# Build the Writer File
docker build -t aekau21/writer:1.0 -f Dockerfile-writer .
docker run --rm -v $PWD/data:/data aekau21/writer:1.0 writer.py/data/data.txt
 
# Build the Computer File
docker build -t aekau21/computer:1.0 -f Dockerfile-computer.
docker run --rm -v $PWD/data:/data aekau21/computer:1.0 computer.py /data/data.txt /data/results.txt

# Build the Website
docker build -t aekau21/website:1.0 -f Dockerfile-website .
docker run --rm -p 8000:8000  -v $PWD/data:/data aekau21/website:1 python -m http.server

 
