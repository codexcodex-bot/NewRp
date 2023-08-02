```python
from sqlalchemy import Column, Integer, String, Float
from website_project.utils.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String(200), nullable=True)

    def __init__(self, name, description, price, image_url=None):
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url

    def __repr__(self):
        return f'<Product {self.name}>'
```