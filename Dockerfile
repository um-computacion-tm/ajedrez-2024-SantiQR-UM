FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-SantiQR-UM.git

WORKDIR /ajedrez-2024-SantiQR-UM

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.interface"]

# docker buildx build -t ajedrez-santiqr .
# docker run -i ajedrez-santiqr

# If it's building a previous version, you can use the following command:
# docker buildx build --no-cache -t ajedrez-santiqr .
