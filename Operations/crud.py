class Operations:
    def create():
        create_temp = f"create table if not exists pet(pet_id serial primary key,pet_name varchar , pet_owner varchar,pet_breed varchar) ;"
        return create_temp
    def display():
        disp_temp = f"select * from pet ;"
        return disp_temp
    def insert(pet_name,pet_owner,pet_breed):
        insert_temp = f"insert into pet(pet_name,pet_owner,pet_breed) values ('{pet_name}','{pet_owner}','{pet_breed}') ;"
        return insert_temp
    def delete(pet_id):
        del_temp = f"delete from pet where pet_id={pet_id};"
        return del_temp
    def update(pet_id,pet_name,pet_owner,pet_breed):
        upd_temp = f"update pet set pet_name ='{pet_name}', pet_owner='{pet_owner}', pet_breed ='{pet_breed}' where pet_id = {pet_id};"
        return upd_temp
    
