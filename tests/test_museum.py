import pytest
import requests
from pydantic import ValidationError

from tests.models.art_model import ArtModel
from tests.models.keyword_model import KeywordModel

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1/"


# Тесты начинаются здесь:
def test_museum_api_status():
    url = f"{BASE_URL}objects/1"
    response = requests.get(url)

    test_art = ArtModel(
        objectID=1,
        isHighlight=False,
        accessionNumber="1979.486.1",
        accessionYear="1979",
        isPublicDomain=False,
        primaryImage="",
        primaryImageSmall="",
        additionalImages=[],
        constituents=[
            {
                "constituentID": 164292,
                "role": "Maker",
                "name": "James Barton Longacre",
                "constituentULAN_URL": "http://vocab.getty.edu/page/ulan/500011409",
                "constituentWikidata_URL": "https://www.wikidata.org/wiki/Q3806459",
                "gender": ""
            }
        ],
        department="The American Wing",
        objectName="Coin",
        title="One-dollar Liberty Head Coin",
        culture="",
        period="",
        dynasty="",
        reign="",
        portfolio="",
        artistRole="Maker",
        artistPrefix="",
        artistDisplayName="James Barton Longacre",
        artistDisplayBio="American, Delaware County, Pennsylvania 1794–1869 Philadelphia, Pennsylvania",
        artistSuffix="",
        artistAlphaSort="Longacre, James Barton",
        artistNationality="American",
        artistBeginDate="1794",
        artistEndDate="1869",
        artistGender="",
        artistWikidata_URL="https://www.wikidata.org/wiki/Q3806459",
        artistULAN_URL="http://vocab.getty.edu/page/ulan/500011409",
        objectDate="1853",
        objectBeginDate=1853,
        objectEndDate=1853,
        medium="Gold",
        dimensions="Dimensions unavailable",
        creditLine="Gift of Heinz L. Stoppelmann, 1979",
        geographyType="",
        city="",
        state="",
        county="",
        country="",
        region="",
        subregion="",
        locale="",
        locus="",
        excavation="",
        river="",
        classification="",
        rightsAndReproduction="",
        linkResource="",
        metadataDate="2021-04-06T04:41:04.967Z",
        repository="Metropolitan Museum of Art, New York, NY",
        objectURL="https://www.metmuseum.org/art/collection/search/1",
        tags=None,
        objectWikidata_URL="",
        isTimelineWork=False,
        GalleryNumber=""
    )
    assert response.status_code == 200

    try:
        data = response.json()
        exp = ArtModel(**data)
        assert exp == test_art
    except ValidationError as e:
        pytest.fail(f"Data validation failed: {e}")


def test_museum_api_nonexistent_id():
    nonexistent_id = 12345678
    url = f"{BASE_URL}objects/{nonexistent_id}"
    response = requests.get(url)
    assert response.status_code == 404


def test_museum_api_search_by_keyword():
    keyword = "Ruble"
    url = f"{BASE_URL}search?q={keyword}"
    response = requests.get(url)
    assert response.status_code == 200

    try:
        data = response.json()
        test_result = KeywordModel(
            total=10,
            objectIDs=[
                459371,
                459370,
                339702,
                437442,
                339701,
                436833,
                423146,
                238319,
                393243,
                471883
            ]

        )

        result = KeywordModel(**data)

        assert result == test_result
    except AssertionError as e:
        pytest.fail(f"Поиск по ключевому слову не удался: {e}")


