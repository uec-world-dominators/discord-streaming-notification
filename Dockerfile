FROM python:3.10

RUN pip install aiohttp discord.py
COPY main.py .
CMD [ "python", "-u", "main.py" ]
