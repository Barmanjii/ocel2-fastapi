# SQL-Alchemy Import
from sqlalchemy.orm import Session

# Local Backend Imports
from app.custom_logger import logger
from app.models.request_model import RequestModel
from app.db.entity.event_entity import EventEntity
from app.db.entity.qualifier import QualifierEntity
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
    async def create(self, db: Session, obj_in: RequestModel):
        if db.in_transaction():
            db.rollback()
            logger.info("Rolled Back the Previous Session")

        try:
            db.begin()
            logger.info("Started the Transcation!!!")

            db_event_type = EventTypeEntity(
                name=obj_in.event_types[0].name,
            )

            db.add(db_event_type)
            db.flush()
            logger.info("Added the Event type")

            db_event_attribute = EventAttributeEntity(
                event_type_id=db_event_type.event_type_id,
                name=obj_in.event_types[0].attributes[0].name,
            )
            db.add(db_event_attribute)
            db.flush()
            logger.info("Added the Event Attribute")

            db_object_type = ObjectTypeEntity(
                name=obj_in.object_types[0].name,
            )

            db.add(db_object_type)
            db.flush()
            logger.info("Added the Object Type")

            db_object_attribute = ObjectAttributeEntity(
                object_type_id=db_object_type.object_type_id,
                name=obj_in.object_types[0].attributes[0].name,
            )
            db.add(db_object_attribute)
            db.flush()
            logger.info("Added the Obect Attribute")

            db_event = EventEntity(
                event_type_id=db_event_type.event_type_id,
                timestamp=obj_in.events[0].timestamp,
            )
            db.add(db_event)
            db.flush()
            logger.info("Added Event")

            db_event_attribute_value = EventAttributeValueEntity(
                event_attribute_id=db_event_attribute.event_attribute_id,
                event_id=db_event.event_id,
                value=obj_in.events[0].attribute_values[0].value,
            )
            db.add(db_event_attribute_value)
            db.flush()
            logger.info("Added Event Attribute Value")

            db_qualifier = QualifierEntity(
                value=obj_in.events[0].relationships_qualifer[0].value,
            )
            db.add(db_qualifier)
            db.flush()
            logger.info("Added Qualifier Value")

            db_object = ObjectEntity(object_type_id=db_object_type.object_type_id)
            db.add(db_object)
            db.flush()
            logger.info("Added Object")

            db_event_object_relationship = EventObjectRelationshipEntity(
                event_id=db_event.event_id,
                object_id=db_object.object_id,
                qualifier_id=db_qualifier.qualifier_id,
            )
            db.add(db_event_object_relationship)
            db.flush()
            logger.info("Added Event Object Relationship")

            db_object_attribute_value = ObjectAttributeValueEntity(
                object_attribute_id=db_object_attribute.object_attribute_id,
                object_id=db_object.object_id,
                timestamp=obj_in.objects[0].timestamp,
                value=obj_in.objects[0].value,
            )
            db.add(db_object_attribute_value)
            db.flush()
            logger.info("Added Object Attribute Value")

            db_object_relationship = ObjectRelationshipEntity(
                object_parent_id=db_object.object_id,
                object_child_id=db_object.object_id,
                qualifier_id=db_qualifier.qualifier_id,
            )
            db.add(db_object_relationship)
            db.flush()
            logger.info("Added Object Relationship")

            db.commit()
            logger.info("Done Adding all the data into the Database..!!!")
            return
        except Exception as e:
            logger.error(f"Rolling back due to this Exception : {str(e)}")
            db.rollback()
            return e


requestObj = CRUDRequest()
