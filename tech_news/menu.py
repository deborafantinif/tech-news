# Requisito 12
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (search_by_category,
                                              search_by_date, search_by_tag,
                                              search_by_title)
from tech_news.scraper import get_tech_news


def analyzer_menu():
    menu = input(
        """Selecione uma das opções a seguir:
        0 - Popular o banco com notícias;
        1 - Buscar notícias por título;
        2 - Buscar notícias por data;
        3 - Buscar notícias por tag;
        4 - Buscar notícias por categoria;
        5 - Listar top 5 notícias;
        6 - Listar top 5 categorias;
        7 - Sair."""
    )
    while input != 7:
        match menu:
            case "0":
                amount = input("Digite quantas notícias serão buscadas:")
                return get_tech_news(amount)
            case "1":
                title = input("Digite o título:")
                return search_by_title(title)
            case "2":
                data = input("Digite a data no formato aaaa-mm-dd:")
                return search_by_date(data)
            case "3":
                tag = input("Digite a tag:")
                return search_by_tag(tag)
            case "4":
                category = input("Digite a categoria:")
                return search_by_category(category)
            case "5":
                return top_5_news()
            case "6":
                return top_5_categories()
            case _:
                return "Opção inválida"
