def create_post_payload(title = "i am nijesh mannuel", price = 199,category= "vintage"):
    return {
         "title": title,
        "price": price,
        "category": category
    }

def create_put_payload(title= "i am nijesh mannuel"):
    return {
        "title": title
    }