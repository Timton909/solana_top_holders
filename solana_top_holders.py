import requests

def top_holders(mint: str, limit: int = 10):
    url = f"https://api.solscan.io/token/holders?token={mint}&offset=0&size={limit}"
    holders = requests.get(url).json()["data"]
    print(f"Top {limit} holders:\n")
    for h in holders:
        pct = h["amount"] / requests.get(f"https://api.solscan.io/token/meta?token={mint}").json()["data"]["supply"] * 100
        print(f"{h['owner'][:10]}... | {h['amount']/1e9:.2f} tokens | {pct:.2f}%")

if __name__ == "__main__":
    token = input("Mint address: ").strip()
    top_holders(token)
