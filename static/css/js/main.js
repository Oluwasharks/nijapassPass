let balance = parseInt(localStorage.getItem('nijaBal') || '50000');
function updateBal(){
  document.querySelectorAll('#walletBal, #walletBal2').forEach(e=>{if(e) e.innerText = balance.toLocaleString()});
  localStorage.setItem('nijaBal', balance);
}
function fundWallet(){
  let amt = prompt("Fund NijaPass Wallet - Enter amount (NGN):","200000");
  if(!amt) return;
  balance += parseInt(amt);
  updateBal();
  alert(`Success! Wallet funded.\nNew Balance: ₦${balance.toLocaleString()}`);
}
function resetWallet(){ if(confirm("Reset wallet?")){ balance=0; updateBal(); } }
function bookItem(name, price, type){
  if(balance < price){
    alert(`Insufficient balance! ${name} costs ₦${price.toLocaleString()} but you have ₦${balance.toLocaleString()}. Please fund wallet.`);
    fundWallet(); return;
  }
  if(confirm(`Confirm Booking:\n\n${name}\nAmount: ₦${price.toLocaleString()}\nPay with NijaPass Wallet?\n\nYour balance: ₦${balance.toLocaleString()}`)){
    balance -= price;
    updateBal();
    alert(`✅ BOOKED!\n\n${name} confirmed.\n₦${price.toLocaleString()} deducted from wallet.\nRemaining: ₦${balance.toLocaleString()}\n\nReceipt sent to your email. Our agent will call you in 5 mins.`);
    window.location.href = `/book/${type}/${price}/`;
  }
}
function toggleWallet(){ document.getElementById('walletSection').scrollIntoView({behavior:'smooth'}); }
document.addEventListener('DOMContentLoaded', updateBal);