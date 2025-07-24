from utils.assertions import assert_equal_validation_message, assert_url


async def delete_account_and_verify(page, loginhome, deleteaccount):
    await loginhome.delete_button_click()
    msg = await deleteaccount.delete_confirmation_text()
    await assert_equal_validation_message(msg, "Account Deleted!")
    await deleteaccount.continue_button_click()
    await assert_url(page, "https://automationexercise.com/")
