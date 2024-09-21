from httpx import AsyncClient
import pytest
from sqlalchemy import select

from app.documents.models import Document
from app.documents.dao import DocumentDAO


green_apple = [
  {
    "id": 1,
    "text": "С другой стороны рамки и место обучения кадров способствует подготовки и реализации модели развития. Зелёное яблоко. Таким образом реализация намеченных плановых заданий позволяет оценить значение новых предложений. Идейные соображения высшего порядка, а также дальнейшее развитие различных форм деятельности позволяет оценить значение новых предложений. Повседневная практика показывает, что реализация намеченных плановых заданий в значительной степени обуславливает создание модели развития. Таким образом реализация намеченных плановых заданий позволяет оценить значение новых предложений. С другой стороны укрепление и развитие структуры обеспечивает участие в формировании систем массового участия. Таким образом реализация намеченных плановых заданий позволяет оценить значение новых предложений. Значимость этих проблем настолько очевидна, что дальнейшее развитие различных форм деятельности обеспечивает широкому кругу (специалистов) участие в формировании новых предложений.",
    "created_date": "2024-09-21T13:00:00",
    "rubrics": [
      "VK-1603736028819866",
      "VK-64144010029",
      "VK-41686355398"
    ]
  }
]

hello = [
  {
    "id": 3,
    "text": "Всем привет!",
    "created_date": "2024-09-20T10:00:00",
    "rubrics": [
      "VK-8456464583465685",
      "VK-65682348905",
      "VK-17367836741"
    ]
  },
  {
    "id": 2,
    "text": "Привет, это тестовый текст",
    "created_date": "2024-09-21T11:00:00",
    "rubrics": [
      "VK-1236782345687986",
      "VK-34578345778",
      "VK-23782367934"
    ]
  }
]


@pytest.mark.parametrize("search_text,result", [
  ("Зелёное яблоко", green_apple),
  ("Зеленое, яблоко!", green_apple),
  ("яблоко зелёное", green_apple),
  ("привет", hello),
  ("То, чего точно нет в тексте", []),
  ("", []),
])
async def test_search_documents(search_text, result):
    documents = await DocumentDAO.search(search_text=search_text)
    assert len(documents) == len(result)
    
    for i in range(len(documents)):
        assert documents[i].text == result[i]["text"]
    
    
@pytest.mark.parametrize("document_id", [5, 10])
async def test_delete_documents(document_id, session):
    await DocumentDAO.delete_by_id(document_id=document_id)
    
    query = select(Document).filter_by(id=document_id)
    result = await session.execute(query)
    get_deleted = result.scalar_one_or_none()
    assert not get_deleted
    