from utils.assertions import assert_verify_account_created

async def register_new_user_flow(page, home, signup, createaccount, user):
    await home.go_to_signup_page()
    await signup.signup(user)
    await assert_verify_account_created(page)
    await createaccount.continue_button_click()
