import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


def get_news():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(amount)


def get_by_title():
    title = input("Digite o título: ")
    return search_by_title(title)


def get_by_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    return search_by_date(date)


def get_by_category():
    category = input("Digite a categoria: ")
    return search_by_category(category)


def get_top_5():
    return top_5_categories()


def print_exit():
    return "Encerrando script"


OPTIONS = {
    0: get_news,
    1: get_by_title,
    2: get_by_date,
    3: get_by_category,
    4: get_top_5,
    5: print_exit,
}


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.",
    )
    try:
        option = int(option)
        print(OPTIONS[option]())
    except Exception:
        print("Opção inválida", file=sys.stderr)


if __name__ == "__main__":
    analyzer_menu()
