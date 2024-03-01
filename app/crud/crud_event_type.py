# UUID Import
from uuid import UUID

# SQL-Alchemy Import
from sqlalchemy.orm import Session

# Local Backend Imports
from app.db.entity.event_type_entity import EventTypeEntity
from app.models.request_model import EventTypeModel


class CRUDEventType:
    def create(self, db: Session, obj_in: EventTypeModel) -> EventTypeEntity:
        try:
            db_event_type = EventTypeEntity(
                name=obj_in.name,
            )
            db.add(db_event_type)
            db.commit()
            db.refresh(db_event_type)
            return db_event_type
        except Exception as e:
            print(str(e))
            return e


eventType = CRUDEventType()
