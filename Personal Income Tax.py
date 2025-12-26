# Determine personal income tax

# Get user to input there status and taxable income
try:
    user_status = int(input("Enter your corresponding digit:"
                           "0 = single\n"
                            "1 = Married filing jointly or qualifying widow(er)\n"
                            "2 =  married filing separately\n"
                            "3 = head of household\n"))
    user_TI = float(input("Enter your taxable income:"))
    if user_status not in [0,1,2,3]:
            print("Invalid filing status")
    else:
        tax = 0
#single
    if user_status == 0:
        if user_TI <=8350:
            tax = 0.10 * user_TI
        elif user_TI <= 33950:
            tax = 0.10 * 8350 + 0.15 * (user_TI-8350)
        elif user_TI <= 82250:
            tax = (0.10 * 8350 + 0.15 * (33950 - 8350)
                                        + 0.25 * (user_TI -33950))
        elif user_TI <= 171550:
            tax =( 0.10 * 8350 + 0.15 * (33950 - 8350)
            + 0.25 * (82250 - 33950) + 0.28 * (user_TI - 82250))
        elif user_TI <= 372950:
            tax = (0.10 * 8350 + 0.15 * (33950 - 8350)
                + 0.25 * (82250 - 33950) + 0.28 * (171550 - 82250) +
                   0.33 * (user_TI - 171550))
        else:
            tax = (0.10 * 8350 + 0.15 * (33950 - 8350) +
                   + 0.25 * (82250 - 33950) + 0.28 * (171550 - 82250) +
                   0.33 * (372550 - 171550) + 0.35 * (user_TI - 372550))
# Married filing jointly or qualifying widow(er)

    if user_status == 1:
        if user_TI <=16700:
            tax = 0.10 * user_TI
        elif user_TI <= 67900:
            tax = 0.10 * 16700 + 0.15 * (user_TI-16700)
        elif user_TI <= 137050:
            tax = (0.10 * 16700 + 0.15 * (67900 -  16700)
                                        + 0.25 * (user_TI -67900))
        elif user_TI <= 208850:
            tax = (0.10 * 16700 + 0.15 * (67900 - 16700)
            + 0.25 * (137050 - 67900) + 0.28 * (user_TI - 137050))
        elif user_TI <= 372950:
            tax = (0.10 * 16700 + 0.15 * (67900 - 16700)
            + 0.25 * (137050 - 67900) + 0.28 * (208850 - 137050) + 0.33 * (user_TI - 208850))
        else:
            tax =  (0.10 * 16700 + 0.15 * (67900 - 16700)
            + 0.25 * (137050 - 67900) + 0.28 * (208850 - 137050) + 0.33 * (372950- 208850) + 0.35 *(user_TI - 372950))
    # Married filing separately
        if user_status == 2:
            if user_TI <= 8350:
                tax = 0.10 * user_TI
            elif user_TI <= 33950:
                tax = 0.10 * 8350 + 0.15 * (user_TI - 8350)
            elif user_TI <= 68525:
                tax = (0.10 * 8350 + 0.15 * (33950 - 8350)
                       + 0.25 * (user_TI - 33950))
            elif user_TI <= 104425:
                tax = (0.10 * 8350 + 0.15 * (33950 - 8350)
                       + 0.25 * (68526 - 33950) + 0.28 * (user_TI - 68526))
            elif user_TI <= 186475:
                tax = (0.10 * 8350 + 0.15 * (33950 - 8350)
                       + 0.25 * (68526 - 33950) + 0.28 * (104425 - 68526) +
                       0.33 * (user_TI - 104425))
            else:
                tax = (0.10 * 8350 + 0.15 * (33950 - 8350)
                       + 0.25 * (68526 - 33950) + 0.28 * (186476 - 68526) +
                       0.33 * (186476 - 104425) +0.35 + (user_TI - 186476))
    # Head of Household
    if user_status == 3:
        if user_TI <= 11950:
            tax = 0.10 * user_TI
        elif user_TI <= 45500:
            tax = 0.10 * 11950 + 0.15 * (user_TI - 11950)
        elif user_TI <= 117450:
            tax = (0.10 * 8350 + 0.15 * (45500 - 11950)
                   + 0.25 * (user_TI - 45500))
        elif user_TI <= 190200:
            tax = (0.10 * 8350 + 0.15 * (45500 - 11950)
                   + 0.25 * (117450 - 45500)+ 0.28 * (user_TI - 117451))
        elif user_TI <= 190201:
            tax = (0.10 * 8350 + 0.15 * (45500 - 11950)
                   + 0.25 * (117450 - 45500)+ 0.28 * (190200 - 117451) + 0.33*( user_TI - 190200))
        else:
            tax = (0.10 * 8350 + 0.15 * (45500 - 11950)
                   + 0.25 * (117450 - 45500)+ 0.28 * (190200 - 117451) + 0.33*( user_TI - 190200))

    print(f"Your tax is: {tax}")

except ValueError: print("Please enter only numbers!")

