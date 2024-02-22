# Logging Import
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
