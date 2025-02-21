from transformers import AutoTokenizer
from datasets import load_from_disk, DatasetDict
import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk,DatasetDict
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_examples_to_features(self, example_batch):
        # Input validation
        if 'dialogue' not in example_batch or 'summary' not in example_batch:
            raise KeyError("Required keys 'dialogue' and 'summary' not found in the dataset")
        
        # Process dialogues
        dialogues = example_batch['dialogue']
        # Ensure dialogues are in list format and all elements are strings
        if isinstance(dialogues, (list, tuple)):
            dialogues = [str(d) for d in dialogues]
        else:
            dialogues = [str(dialogues)]
            
        # Tokenize dialogues
        input_encodings = self.tokenizer(
            dialogues,
            max_length=1024,
            truncation=True,
            padding='max_length',
            return_tensors=None  # Return lists instead of tensors
        )
        
        # Process summaries
        summaries = example_batch['summary']
        # Ensure summaries are in list format and all elements are strings
        if isinstance(summaries, (list, tuple)):
            summaries = [str(s) for s in summaries]
        else:
            summaries = [str(summaries)]
        
        # Tokenize summaries
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                summaries,
                max_length=128,
                truncation=True,
                padding='max_length',
                return_tensors=None  # Return lists instead of tensors
            )
        
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        try:
            # Load dataset
            dataset_samsum = load_from_disk(self.config.data_path)
            print("Dataset loaded successfully")
            print("Dataset structure:", dataset_samsum)
            
            # Create output directory
            output_dir = os.path.join(self.config.root_dir, "samsum_dataset")
            os.makedirs(output_dir, exist_ok=True)
            
            # Initialize transformed dataset
            transformed_dataset = DatasetDict()
            
            # Process each split
            for split in dataset_samsum.keys():
                print(f"\nProcessing {split} split...")
                
                # Print sample for debugging
                print(f"Sample entry from {split}:", dataset_samsum[split][0])
                
                # Transform the split with error handling
                try:
                    transformed_split = dataset_samsum[split].map(
                        self.convert_examples_to_features,
                        batched=True,
                        batch_size=8,  # Smaller batch size for better error handling
                        desc=f"Processing {split} split",
                        remove_columns=dataset_samsum[split].column_names  # Remove original columns
                    )
                    
                    # Add to transformed dataset
                    transformed_dataset[split] = transformed_split
                    print(f"Successfully processed {split} split")
                    
                except Exception as e:
                    print(f"Error processing {split} split: {str(e)}")
                    raise
            
            # Save transformed dataset
            transformed_dataset.save_to_disk(output_dir)
            print(f"\nTransformed dataset saved to {output_dir}")
            
            return transformed_dataset
            
        except Exception as e:
            print(f"Error in convert method: {str(e)}")
            raise