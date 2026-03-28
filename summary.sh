#!/bin/bash

echo "Starting pipeline..."

# Run the container and execute the full pipeline
docker run -it --name olist-container \
  -v "$(pwd)/results:/app/pipeline/results" \
  olist-pipeline \
  bash -c "python ingest.py olist_merged.csv && cp data_preprocessed.csv results/ && cp insight1.txt results/ && cp insight2.txt results/ && cp insight3.txt results/ && cp summary_plot.png results/ && cp clusters.txt results/ && echo '✅ All files copied to results/'"

echo "Stopping and removing container..."
docker stop olist-container 2>/dev/null
docker rm olist-container 2>/dev/null

echo "Done! Check your results/ folder!"