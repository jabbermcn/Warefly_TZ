from fastapi import FastAPI
from word_counter import read_large_file

app = FastAPI()


@app.get("/")
async def main_page():
    return f"Тестовое задание Warefly"


@app.get("/getWords")
async def get_words():
    word_counts = read_large_file('dump/lenta-ru-news.csv')
    top_100_words = word_counts.most_common(100)
    return top_100_words
