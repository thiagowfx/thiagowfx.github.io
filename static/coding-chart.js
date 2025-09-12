document.addEventListener('DOMContentLoaded', function() {
  if (typeof codingPostDates === 'undefined') {
    console.error('coding-chart.js: codingPostDates not defined');
    return;
  }
  if (typeof otherCodingPostDates === 'undefined') {
    console.error('coding-chart.js: otherCodingPostDates not defined');
    return;
  }

  // Helper function to process date arrays
  const processDates = (dates) => {
    const sorted = dates.filter(d => d).sort();
    const cumulative = {};
    sorted.forEach((date, index) => {
      cumulative[date] = index + 1;
    });
    return {
      sorted,
      cumulative
    };
  };

  const leetCodeData = processDates(codingPostDates);
  const otherData = processDates(otherCodingPostDates);

  // Determine the overall date range
  const allDates = leetCodeData.sorted.concat(otherData.sorted).sort();
  if (allDates.length === 0) {
    return; // No data to plot
  }
  const firstDate = new Date(allDates[0]);
  const lastDate = new Date(allDates[allDates.length - 1]);

  // Generate all date labels for the x-axis
  const dateLabels = [];
  let currentDate = new Date(firstDate);
  while (currentDate <= lastDate) {
    dateLabels.push(currentDate.toISOString().split('T')[0]);
    currentDate.setDate(currentDate.getDate() + 1);
  }

  // Generate cumulative values for both datasets
  const cumulativeValuesLeetCode = [];
  const cumulativeValuesOther = [];
  let leetCodeCount = 0;
  let otherCount = 0;

  dateLabels.forEach(dateStr => {
    if (leetCodeData.cumulative[dateStr]) {
      leetCodeCount = leetCodeData.cumulative[dateStr];
    }
    cumulativeValuesLeetCode.push(leetCodeCount);

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
        label: 'LeetCode Problems Solved',
        data: cumulativeValuesLeetCode,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
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
