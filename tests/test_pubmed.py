from poldracklab.pubmed import (
    run_pubmed_query,
    parse_pubmed_query_result,
)
import pytest


@pytest.fixture
def pubmed_query_result():
    return run_pubmed_query(
        "'Badomics words and the power and peril of the ome-meme'", "test@test.com"
    )


@pytest.fixture
def parsed_pubmed_query_result(pubmed_query_result):
    return parse_pubmed_query_result(pubmed_query_result)


@pytest.fixture
def pubmed_record(parsed_pubmed_query_result):
    return list(parsed_pubmed_query_result.values())[0]


def test_get_pubmed_data(pubmed_query_result):
    assert len(pubmed_query_result) > 0
    assert "PubmedArticle" in pubmed_query_result
    assert "MedlineCitation" in pubmed_query_result["PubmedArticle"][0]
    assert "PMID" in pubmed_query_result["PubmedArticle"][0]["MedlineCitation"]


def test_parse_pubmed_query_result(parsed_pubmed_query_result):
    assert len(parsed_pubmed_query_result) == 1


def test_parse_pubmed_pubs(pubmed_record):
    assert "DOI" in pubmed_record
    assert pubmed_record["DOI"] == "10.1186/2047-217x-1-6"
    assert "title" in pubmed_record
    assert (
        pubmed_record["title"]
        == "Badomics words and the power and peril of the ome-meme."
    )
    assert "journal" in pubmed_record
    assert pubmed_record["journal"] == "Gigascience"
    assert "PMID" in pubmed_record
    assert pubmed_record["PMID"] == 23587201
