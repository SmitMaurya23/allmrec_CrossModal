import json

# Path to the Amazon review data and metadata files
review_data_file = 'Movies_and_TV.json'
metadata_file = 'meta_Movies_and_TV.json'
output_file = 'filtered_Movies_and_TV.json'

# Step 1: Load ASINs from the metadata file
metadata_asins = set()
with open(metadata_file, 'r') as meta_file:
    for line in meta_file:
        meta_item = json.loads(line)
        asin = meta_item.get('asin')
        if asin:
            metadata_asins.add(asin)

print(f"Loaded {len(metadata_asins)} ASINs from metadata.")

# Step 2: Traverse the review dataset and filter it based on ASINs in the metadata
with open(review_data_file, 'r') as review_file, open(output_file, 'w') as out_file:
    for line in review_file:
        review = json.loads(line)
        asin = review.get('asin')
        
        if asin and asin in metadata_asins:
            out_file.write(json.dumps(review) + '\n')  # Write matching reviews to output file

print(f"Filtered reviews written to {output_file}.")
