from restraunt import Restaurant

res = Restaurant("Tehzeeb" , "Pakistani")
res.describe_restaurant()
res.open_restaurant()

from Admin import Admin

ad = Admin("Hassan" , "Ali")
ad.privileges = "Can ban "
ad.privileges = "Can Dismis "
ad.show_privileges()

