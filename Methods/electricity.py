def bill(watts, rate):
    return watts * rate

    
def bill_with_gst(watts, rate, gst_rate):
    amount = bill(watts, rate)
    return gst(amount, gst_rate)