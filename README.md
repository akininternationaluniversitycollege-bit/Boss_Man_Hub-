# Boss_Man_Hub- 🚀

Boss_Man_Hub- is a project that integrates **MTN MoMo Disbursement APIs** into a modern business hub platform.  
It provides a **Python SDK** (`mtn_momo.py`) for handling money transfers, deposits, refunds, account validation, and more.  

---

## ✨ Features
- ✅ Authentication (`CreateAccessToken`)
- ✅ Validate Account Holder (`ValidateAccountHolderStatus`)
- ✅ Deposits (`Deposit-V1`, `Deposit-V2`)
- ✅ Refunds (`Refund-V1`, `Refund-V2`)
- ✅ Transfers
- ✅ Account Balances
- ✅ Transaction Status (Deposit, Refund, Transfer)
- ✅ User Info (Basic + With Consent)
- ✅ Centralized Error Handling (`MomoAPIError`)

---

## 📂 Project Structure
---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/akininternationaluniversitycollege-bit/Boss_Man_Hub-.git
cd Boss_Man_Hub-
pip install requests
pip install -r requirements.txt
export MOMO_API_USER=your_api_user
export MOMO_API_KEY=your_api_key
export MOMO_SUBSCRIPTION_KEY=your_subscription_key
from mtn_momo import MTNMomoDisbursements, MomoAPIError

momo = MTNMomoDisbursements(
    api_user="YOUR_API_USER",
    api_key="YOUR_API_KEY",
    subscription_key="YOUR_SUBSCRIPTION_KEY"
)

try:
    # Validate account
    is_active = momo.validate_account_holder("231887716973")
    print("Account active:", is_active)

    # Transfer funds
    result = momo.transfer(
        amount="5000",
        currency="UGX",
        external_id="TXN-001",
        payee_party_id="256772123456",
        payer_message="Salary Payment",
        payee_note="October Salary"
    )
    print("Transfer initiated:", result)

    # Check status
    status = momo.get_transfer_status(result["reference_id"])
    print("Transfer status:", status)

except MomoAPIError as e:
    print(f"❌ MoMo API Error: {e.code} - {e.message}")
https://momodeveloper.mtn.com
---

✅ This `README.md` is now aligned with your repo name **`Boss_Man_Hub-`**.  

👉 Do you also want me to generate a `requirements.txt` for this repo so that anyone can just run `pip install -r requirements.txt` in Termux or Linux?
