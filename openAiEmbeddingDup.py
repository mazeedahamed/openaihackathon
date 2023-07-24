import openai, numpy as np, os

os.environ["OPENAI_API_KEY"] = ''
openai.api_key = os.getenv("OPENAI_API_KEY")

disc1="This trade confirmation is provided solely for informational purposes. It is not an offer, recommendation, or solicitation to buy or sell any security. All investments involve risk, including the loss of principal. The price, value, and income of any security or instrument may fluctuate and you may lose money. You should not rely on the information contained herein as the basis for making any investment decisions. It is important to speak with an investment professional prior to making any investment decisions."

disc2="Disclosures or Disclaimer:  Fixed income securities (bonds) are traded over the counter (OTC) and not through an exchange like equity securities.The firm's mark-up or mark-down on your transaction is measured from the prevailing market price for the fixed income security.The prevailing market price is determined by application of a series of factors prescribed by industry regulators (FINRA and MSRB) and may not be the same as the firm's cost of sourcing, or its proceeds from selling, the security.As such, industry participants may come to different determinations concerning the prevailing market price of any given fixed income security at any point in time.In addition, the mark-up or mark-down is not necessarily the same as the firm's profit or loss on the transaction, which may be impacted by a number of other factors, such as out-of-pocket costs, namely regulatory fees and hedging costs, and intervening market movements, among others factors, that do not impact the prevailing market price and/or the calculated mark-up or mark-down.The firm has engaged a third party vendor to calculate the prevailing market price in accordance with FINRA and MSRB rules."
disc3="The price and share totals shown above reflect the price received for the trade date. Due to market operating hour differences, the trade date may be after the date your order was placed with us for certain funds. Contact us for additional information. We are providing information to all offshore investors, to advise that there is a key investor information document (KIID) available for each fund offered by offshore (non-us domiciled) investment companies regulated as undertaking for collective investments in transferable securities (UCITs). The KIID contains essential information and key facts about a UCITS fund aimed at helping investors make informed investment decisions about whether the fund meets their needs. Please read the KIID carefully before you invest. You can access a repository of KIID documents at the following location www.morganstanley.com/offshoremutualfunds/kiidrepository. For UCITS mutual funds and the following web location https://www.morganstanley.com/disclaimers/etfkiidrepository For UCITS exchange-traded funds. For further information about the fund, please refer to the fund's prospectus."
resp = openai.Embedding.create(
    input=[disc1, disc2, disc3],
    engine="text-similarity-davinci-001")

embedding_a = resp['data'][0]['embedding']
embedding_b = resp['data'][1]['embedding']
embedding_c = resp['data'][2]['embedding']
similarity_score_ab = np.dot(embedding_a, embedding_b)
similarity_score_ac = np.dot(embedding_a, embedding_c)
print("similarity score of disc1 and disc2:  " + str(similarity_score_ab))
print("similarity score of disc1 and disc3:  " + str(similarity_score_ac))