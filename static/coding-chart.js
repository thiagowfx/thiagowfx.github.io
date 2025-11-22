document.addEventListener('DOMContentLoaded', function() {
  if (typeof leetCodePostDates === 'undefined') {
    console.error('coding-chart.js: leetCodePostDates not defined');
    return;
  }
  if (typeof byteByteGoPostDates === 'undefined') {
    console.error('coding-chart.js: byteByteGoPostDates not defined');
    return;
  }
  if (typeof otherCodingPostDates === 'undefined') {
    console.error('coding-chart.js: otherCodingPostDates not defined');
    return;
  }

  // Helper function to process date arrays - builds cumulative counts from all history
  const processDates = (dates) => {
    const sorted = dates.filter(d => d).sort();
    const cumulative = {};
    sorted.forEach((date, index) => {
      cumulative[date] = index + 1;
    });
    return {
      sorted,
      cumulative,
      totalCount: sorted.length
    };
  };

  const leetCodeData = processDates(leetCodePostDates);
  const byteByteGoData = processDates(byteByteGoPostDates);
  const otherData = processDates(otherCodingPostDates);

  // Determine the date range (last month only for display)
  const allDates = leetCodeData.sorted.concat(byteByteGoData.sorted).concat(otherData.sorted).sort();
  if (allDates.length === 0) {
    return; // No data to plot
  }
  const lastDate = new Date(allDates[allDates.length - 1]);
  const firstDate = new Date(lastDate);
  firstDate.setMonth(firstDate.getMonth() - 1);

  // Generate all date labels for the x-axis (last month only)
  const dateLabels = [];
  let currentDate = new Date(firstDate);
  while (currentDate <= lastDate) {
    dateLabels.push(currentDate.toISOString().split('T')[0]);
    currentDate.setDate(currentDate.getDate() + 1);
  }

  // Calculate initial counts (all posts before the display window)
  let leetCodeCount = 0;
  let byteByteGoCount = 0;
  let otherCount = 0;

  const firstDateStr = dateLabels[0];
  leetCodeData.sorted.forEach(date => {
    if (date < firstDateStr) leetCodeCount++;
  });
  byteByteGoData.sorted.forEach(date => {
    if (date < firstDateStr) byteByteGoCount++;
  });
  otherData.sorted.forEach(date => {
    if (date < firstDateStr) otherCount++;
  });

  // Generate cumulative values for all datasets (starting from historical count)
  const cumulativeValuesLeetCode = [];
  const cumulativeValuesByteByteGo = [];
  const cumulativeValuesOther = [];

  dateLabels.forEach(dateStr => {
    if (leetCodeData.cumulative[dateStr]) {
      leetCodeCount = leetCodeData.cumulative[dateStr];
    }
    cumulativeValuesLeetCode.push(leetCodeCount);

    if (byteByteGoData.cumulative[dateStr]) {
      byteByteGoCount = byteByteGoData.cumulative[dateStr];
    }
    cumulativeValuesByteByteGo.push(byteByteGoCount);

    if (otherData.cumulative[dateStr]) {
      otherCount = otherData.cumulative[dateStr];
    }
    cumulativeValuesOther.push(otherCount);
  });

  // Create chart
  const ctx = document.getElementById('cumulative-chart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: dateLabels,
      datasets: [{
        label: 'LeetCode Problems',
        data: cumulativeValuesLeetCode,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.1,
        fill: true
      }, {
        label: 'ByteByteGo Problems',
        data: cumulativeValuesByteByteGo,
        borderColor: 'rgb(255, 159, 64)',
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
        tension: 0.1,
        fill: true
      }, {
        label: 'Other Coding Posts',
        data: cumulativeValuesOther,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        tension: 0.1,
        fill: true
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Cumulative Coding Posts Over Time'
        },
        legend: {
          display: true
        }
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Date'
          }
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Cumulative Posts'
          },
          ticks: {
            stepSize: 1
          }
        }
      },
      interaction: {
        intersect: false,
        mode: 'index'
      }
    }
  });
});
