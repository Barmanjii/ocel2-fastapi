# SQL-Alchemy Import
from sqlalchemy.orm import Session

# Local Backend Imports
from app.models.request_model import RequestModel
from app.db.entity.qualifier import qualifierEntity
from app.db.entity.event_entity import EventEntity
from app.db.entity.object_entity import ObjectEntity
from app.db.entity.event_type_entity import EventTypeEntity
from app.db.entity.object_type_entity import ObjectTypeEntity
from app.db.entity.event_attribute_entity import EventAttributeEntity
from app.db.entity.object_relationship import ObjectRelationshipEntity
from app.db.entity.object_attribute_entity import ObjectAttributeEntity
from app.db.entity.event_attribute_value_entity import EventAttributeValueEntity
from app.db.entity.event_object_relationship import EventObjectRelationshipEntity
from app.db.entity.object_attribute_value_entity import ObjectAttributeValueEntity


class CRUDRequest:
    def create(self, db: Session, obj_in: RequestModel):
        if db.in_transaction():
            db.rollback()
        try:
            db.begin()
            db_event_type = EventTypeEntity(
                name=obj_in.event_type.name,
            )

            db.add(db_event_type)
            db.flush()

            db_event = EventEntity(
                event_type_id=db_event_type.event_type_id,
                timestamp=obj_in.event.timestamp,
            )
            db.add(db_event)
            db.flush()

            db_event_attribute = EventAttributeEntity(
                event_type_id=db_event_type.event_type_id,
                name=obj_in.event_attribute.name,
            )
            db.add(db_event_attribute)
            db.flush()

            db.commit()
            return
        except Exception as e:
            print(str(e))
            db.rollback()
            return e


requestObj = CRUDRequest()
