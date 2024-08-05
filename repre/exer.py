total_reviews = 0

# Check if the total number of reviews is already obtained
if 'total_reviews' not in meta_field:
    # If not, then obtain the total number of reviews from the meta field
    total_reviews = get_total_reviews_from_meta_field(meta_field)
else:
    # If already obtained, then use the existing value
    total_reviews = meta_field['total_reviews']

# Use the total_reviews variable for further processing
print("Total number of reviews: ", total_reviews)
