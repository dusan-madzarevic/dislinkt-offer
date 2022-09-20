db.createUser({
    user: 'root',
    pwd: 'password',
    roles: [
        {
            role: 'readWrite',
            db: 'offers',
        },
    ],
});

db = new Mongo().getDB("offers");

db.createCollection('offer', { capped: false });
