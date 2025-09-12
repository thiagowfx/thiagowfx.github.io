document.addEventListener('DOMContentLoaded', function() {
  // LeetCode posts data (will be populated by Hugo template)
  if (typeof codingPostDates === 'undefined') {
    console.error('coding-chart.js: codingPostDates not defined');
    return;
  }

  // Remove trailing comma and sort dates
  const sortedDates = codingPostDates.filter(d => d).sort();

  // Create cumulative data
  const cumulativeData = {};
  sortedDates.forEach((date, index) => {
    cumulativeData[date] = index + 1;
  });

  // Generate all dates from first post to last post
  const firstDate = new Date(sortedDates[0]);
  const lastDate = new Date(sortedDates[sortedDates.length - 1]);
  const dateLabels = [];
  const cumulativeValues = [];

  let currentDate = new Date(firstDate);
  let cumulativeCount = 0;

  while (currentDate <= lastDate) {
    const dateStr = currentDate.toISOString().split('T')[0];
    dateLabels.push(dateStr);

    if (cumulativeData[dateStr]) {
      cumulativeCount = cumulativeData[dateStr];
    }

    cumulativeValues.push(cumulativeCount);
    currentDate.setDate(currentDate.getDate() + 1);
  }

  // Create chart
  const ctx = document.getElementById('cumulative-chart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: dateLabels,
      datasets: [{
        label: 'LeetCode Problems Solved',
        data: cumulativeValues,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.1,
        fill: true
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Cumulative LeetCode Problems Solved'
        },
        legend: {
          display: false
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
            text: 'LeetCode Problems Solved'
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
