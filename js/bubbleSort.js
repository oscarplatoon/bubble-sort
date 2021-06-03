function bubbleSort(sequence) {
  let count = 0
  for (let i = 0; i < sequence.length; i++) {
    for (let j = 0; j < sequence.length - i - 1; j++) {
      if (sequence[j] > sequence[j + 1]) {
        //let currentItem = sequence[j]
        //let nextItem = sequence[j + 1]
        let current = sequence[j]
        sequence[j] = sequence[j + 1]
        sequence[j + 1] = current
        count++
      }
    }
  }
  return sequence, count
}


console.log((bubbleSort([1, 7, 8, 6, 3, 2, 4])))