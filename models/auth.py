import jwt

class Auth:
    def __init__(self, email):
        self.valid_email = ["lucas@sheetgo.com", "mauricio@sheetgo.com","rafael@sheetgo.com"]
        self.secret = 'z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00'
        self.header = {'authorization':'Bearer'}
        self.email = email
        self.jwt_token = ""

    def createJwt(self):

        # simple check email
        if self.email in self.valid_email:
            
            # create jwt
            encoded_jwt = jwt.encode({'email': self.email}, self.secret, algorithm='HS256', headers=self.header)            
            self.jwt_token = encoded_jwt

            return True
        else:
            return False
    


        
      