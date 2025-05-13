docker build -f .\docker\Dockerfile -t freex-tts:1 .

docker compose -f "D:\Code\AI\index-tts-fastapi\docker\compose-launch.yaml" up -d
