FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel

WORKDIR /app
ENV TZ=Asia/Shanghai

# Install system dependencies including ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY ../requirements.txt /app/requirements.txt

# Install Python dependencies
# Using --no-cache-dir to reduce image size
# Ensuring pip is up-to-date and installing from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir deepspeed

# Set CUDA environment variables
ENV CUDA_HOME=/usr/local/cuda-12.6
ENV PATH=$CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Copy the rest of the application code
# COPY ../ /app/

EXPOSE 8060
EXPOSE 8066
# Set the entrypoint for the application
ENTRYPOINT ["python", "launch.py"]