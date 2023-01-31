from sqlalchemy import Column, BigInteger, String, Text

from .db_core import Base


class ChatModel(Base):
    __tablename__ = "admin_panel_app_chat"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(50))
    invite_link = Column(String(255))
    greeting_text = Column(Text)
    greeting_image = Column(String(100))
