from otus_search.search import get_links


def test_google_get_links():
    links = get_links(topic='otus', start='google', num=3)
    assert len(links) == 3


def test_yandex_get_links():
    links = get_links(topic='otus', start='yandex', num=3)
    assert len(links) == 3
