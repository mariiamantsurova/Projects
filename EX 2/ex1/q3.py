class Knas:
    default_percent = 110
    def __init__ (self, delay_time_in_days, percent):
        self.delay_time_in_days = delay_time_in_days
        self.percent = percent
        if self.percent < Knas.default_percent:
            self.percent = Knas.default_percent

    def __call__(self, knas_details, original_knas):
        new_knas = original_knas * self.percent/100
        # printing the details:

        print(f"Knas details: {knas_details}")
        print(f"The original knas was: {original_knas}")
        print(f"{self.delay_time_in_days} days have passed since the deadline time to pay.")
        print(f"The new knas is now {new_knas}")
        print(f"You should pay this within 30 days. Thank you.")

# examples:
one_month_delay_115 = Knas(30, 115)
one_month_delay_125 = Knas(30, 125)
two_months_delay_150 = Knas(60, 150)

# Call the instances with the required parameters
one_month_delay_115("Parking in an unauthorized area", 300)
one_month_delay_125("Driving above the speed limit", 500)
two_months_delay_150("Parking on red-white area", 400)


