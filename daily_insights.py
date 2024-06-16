from h2o_wave import site, ui

page = site['/day']

page['example'] = ui.form_card(
    box='1 1 3 -1',
    items=[
        ui.text_xl('Oil Sector 🛢️'),
        ui.text_l('West Texas Intermediate (WTI) Oil'),
        ui.text('Buy: 100 barrels of WTI crude futures at $75.50, with a stop-loss at $72.50 and a target price range of $80-$82.'),
        ui.text('Risk factor: Medium to High'),
        ui.text_xs('Given that WTI settled above $79 a barrel and the market shows signs of tightness, it might be a good opportunity to invest in oil stocks or ETFs that track oil prices. Companies involved in oil production, such as Chevron (CVX), might see a positive impact.'),

        ui.separator(''),
        ui.text_xl('Technology and Semiconductors: 𓇲'),
        ui.text_l('NVIDIA (NVDA)'),
        ui.text('Buy: 2 shares at $250.00, with a stop-loss at $235.00 and a target price range of $275.00-$285.00.'),
        ui.text('Risk factor: Medium to High'),
        # ui.text_xs('With the Qatar Investment Authority planning to invest in Ardian Semiconductor, there seems to be a bullish outlook on the semiconductor industry. Consider investing in semiconductor companies or ETFs focused on this sector.'),

        ui.text_l('Advanced Micro Devices (AMD)'),
        ui.text('Buy: 3 shares at $60.00, with a stop-loss at $55.50 and a target price range of $67.50-$70.00.'),
        ui.text('Risk factor: Low to Medium'),
        #ui.text_xs('The increase in subsidies for the semiconductor industry can drive growth. Investing in major semiconductor players like NVIDIA (NVDA), Intel (INTC), or AMD (AMD) could be beneficial.'),

        ui.text_l('Texas Instruments (TXN)'),
        ui.text('Buy: 2 shares at $170.00, with a stop-loss at $160.50 and a target price range of $185.00-$190.00.'),
        ui.text('Risk factor: Medium'),
        # ui.text_xs('The increase in subsidies for the semiconductor industry can drive growth. Investing in major semiconductor players like NVIDIA (NVDA), Intel (INTC), or AMD (AMD) could be beneficial.'),


    ],
)

page['example2'] = ui.form_card(
    box='4 1 3 -1',
    items=[
        ui.text_xl('Energy Stocks 🔋'),
        ui.text_l('ExxonMobil (XOM)'),
        ui.text('Buy: 10 shares at $65.00, with a stop-loss at $62.50 and a target price range of $72.50-$75.00.'),
        ui.text('Risk factor: Medium'),
        # ui.text_xs(''),
        ui.text_l('Chevron (CVX)'),
        ui.text('Buy: 15 shares at $70.00, with a stop-loss at $67.50 and a target price range of $77.50-$80.00.'),
        ui.text('Risk factor: Medium to High'),

        ui.text_l('Hess (HES)'),
        ui.text('Buy: 5 shares at $45.00, with a stop-loss at $42.50 and a target price range of $52.50-$55.00.'),
        ui.text('Risk factor: Low to Medium'),

        ui.text_l('Goldman Sachs Group (GS)'),
        ui.text('Buy: 10 shares at $325.00, with a stop-loss at $310.00 and a target price range of $345.00-$350.00.'),
        ui.text('Risk factor: High'),

        ui.separator(''),
        ui.text_xl('Meme Stocks 📈'),
        ui.text_l('GameStop (GME)'),
        ui.text('Buy: 5 shares at $20.00, with a stop-loss at $18.50 and a target price range of $25.00-$27.50.'),
        ui.text('Risk factor: Very High'),
        ui.text_xs('With shares soaring due to renewed interest from \'Roaring Kitty,\' there could be short-term trading opportunities in meme stocks like GameStop. However, be cautious as these stocks can be highly volatile.'),

    ],
)

page['example3'] = ui.form_card(
    box='7 1 3 -1',
    items=[
        ui.text_xl('Automotive Industry 🏎️'),
        ui.text_l('GM\'s Cruise'),
        ui.text_xs('With GM\'s Cruise starting to test robotaxis in Phoenix, there is positive momentum in the autonomous vehicle sector. Investing in GM or other companies involved in autonomous driving technology could be advantageous.'),

        ui.separator(''),
        ui.text_xl('Bonds 💴'),
        ui.text_l('John Miller’s Junk Muni Fund'),
        ui.text_xs('The rapid growth of John Miller’s Junk Muni Fund to $1 billion suggests strong interest in high-yield municipal bonds. This could indicate a trend towards higher-yield investments, making it worth considering municipal bond funds for a diversified portfolio.'),

        ui.separator(''),
        ui.text_xl('Market Sentiment'),
        ui.text_l('Goldman\'s Rubner Sees FOMO'),
        ui.text_xs('Fear of missing out (FOMO) ahead of key inflation data indicates a potentially bullish market sentiment. This could be a good time to capitalize on short-term gains by investing in broad market indices or sectors expected to perform well.'),

    ],
)

page.save()
