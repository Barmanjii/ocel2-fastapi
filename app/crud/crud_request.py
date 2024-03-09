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
                name=obj_in.event_type_name,
            )

            db.add(db_event_type)
            db.commit()
            return
        except Exception as e:
            print(str(e))
            db.rollback()
            return e


requestObj = CRUDRequest()
