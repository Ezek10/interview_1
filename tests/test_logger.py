from src.logger import Logger


def test_get_all_logs():
    logger = Logger()
    logger.log("test_1")
    logger.log("test_2")
    assert logger.get_all_logs() == ["test_1", "test_2"]

def test_get_no_log():
    logger = Logger()
    assert logger.get_all_logs() == []

def test_cleaning_logs():
    logger = Logger()
    logger.log("test_1")
    logger.log("test_2")
    logger.clean()
    assert logger.get_all_logs() == []

def test_get_logs_persist_after_clean():
    logger = Logger()
    logger.log("test_1")
    logger.log("test_2")
    logs = logger.get_all_logs()
    logger.clean()
    assert logs == ["test_1", "test_2"]
