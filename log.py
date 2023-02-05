import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('example.log')
fmtr = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmtr)
logger.addHandler(fh)

class Log:
    def log_read(data):
        logger.info(f"User reading the following data {data}")
    def log_update(pet_id,pet_name,pet_owner,pet_breed):
        logger.info(f"User updating the data of {pet_id} to ({pet_name}, {pet_owner}, {pet_breed})")
    def log_delete(pet_id):
        logger.info(f"User deleting the data of  pet id{pet_id}")
    def log_insert(pet_name,pet_owner,pet_breed):
        logger.info(f"Following data is inserted: ({pet_name}, {pet_owner}, {pet_breed})")
    def log_connection(flag):
        if flag:
            logger.info("Connected")
        else:
            logger.info("Not Connected")
    def log_close(flag):
        if flag:
            logger.info("connection is closed")
        else:
            logger.info("connection is not closed")
    def read_log():
       with open('example.log','r') as f:
        data = f.readlines() 
        f.close()
        return data
