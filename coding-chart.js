document.addEventListener('DOMContentLoaded', function() {
  if (typeof leetCodePostDates === 'undefined') {
    console.error('coding-chart.js: leetCodePostDates not defined');
    return;
  }
  if (typeof byteByteGoPostDates === 'undefined') {
    console.error('coding-chart.js: byteByteGoPostDates not defined');
    return;
  }
  if (typeof aocPostDates === 'undefined') {
    console.error('coding-chart.js: aocPostDates not defined');
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
  const aocData = processDates(aocPostDates);
  const otherData = processDates(otherCodingPostDates);

  // Determine the date range (last month only for display)
  const allDates = leetCodeData.sorted.concat(byteByteGoData.sorted).concat(aocData.sorted).concat(otherData.sorted).sort();
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
  let aocCount = 0;
  let otherCount = 0;

  const firstDateStr = dateLabels[0];
  leetCodeData.sorted.forEach(date => {
    if (date < firstDateStr) leetCodeCount++;
  });
  byteByteGoData.sorted.forEach(date => {
    if (date < firstDateStr) byteByteGoCount++;
  });
  aocData.sorted.forEach(date => {
    if (date < firstDateStr) aocCount++;
  });
  otherData.sorted.forEach(date => {
    if (date < firstDateStr) otherCount++;
  });

  // Generate cumulative values for all datasets (starting from historical count)
  const cumulativeValuesLeetCode = [];
  const cumulativeValuesByteByteGo = [];
  const cumulativeValuesAoC = [];
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

    if (aocData.cumulative[dateStr]) {
      aocCount = aocData.cumulative[dateStr];
    }
    cumulativeValuesAoC.push(aocCount);

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
        label: 'LeetCode',
        data: cumulativeValuesLeetCode,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.1,
        fill: true
      }, {
        label: 'ByteByteGo',
        data: cumulativeValuesByteByteGo,
        borderColor: 'rgb(255, 159, 64)',
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
        tension: 0.1,
        fill: true
      }, {
        label: 'Advent of Code',
        data: cumulativeValuesAoC,
        borderColor: 'rgb(155, 89, 182)',
        backgroundColor: 'rgba(155, 89, 182, 0.2)',
        tension: 0.1,
        fill: true
      }, {
        label: 'Other',
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
          text: 'Cumulative coding posts over time'
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
            text: 'Cumulative posts'
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
