// Adapted from: https://developer.mozilla.org/en-US/docs/Web/API/Battery_Status_API
navigator.getBattery().then(function(battery) {
  function updateAllBatteryInfo(){
    updateChargeInfo();
    updateLevelInfo();
    updateChargingInfo();
    updateDischargingInfo();
  }
  updateAllBatteryInfo();

  battery.addEventListener('chargingchange', function(){
    updateChargeInfo();
  });
  function updateChargeInfo(){
    let pre = document.getElementById("charging");
    pre.innerHTML = battery.charging ? "Yes" : "No";
  }

  battery.addEventListener('levelchange', function(){
    updateLevelInfo();
  });
  function updateLevelInfo(){
    let pre = document.getElementById("level");
    pre.innerHTML = battery.level * 100;
  }

  battery.addEventListener('chargingtimechange', function(){
    updateChargingInfo();
  });
  function updateChargingInfo(){
    let pre = document.getElementById("chargingTime");
    pre.innerHTML = battery.chargingTime + " seconds";
  }

  battery.addEventListener('dischargingtimechange', function(){
    updateDischargingInfo();
  });
  function updateDischargingInfo(){
    let pre = document.getElementById("dischargingTime");
    pre.innerHTML = battery.dischargingTime + " seconds";
  }

});