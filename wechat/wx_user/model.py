from run import db

class UsersWeixin(db.Model):
    __tablename__ = 'aws_users_weixin'
    
    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer)
    openid = db.Column(db.String(255))
    expires_in = db.Column(db.Integer)
    access_token = db.Column(db.String(255))
    refresh_token = db.Column(db.String(255))
    scope = db.Column(db.String(64))
    headimgurl = db.Column(db.String(256))
    nickname = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    province = db.Column(db.String(32))
    city = db.Column(db.String(32))
    country = db.Column(db.String(32))
    add_time = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    location_update = db.Column(db.Integer)

