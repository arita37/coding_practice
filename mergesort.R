#' Sory an array using the merge-sort algorithm
#' 
#' @param array An array
#' @return Sorted array.
#' @examples
#' array <- sample(seq(1,10))
#' mergesort(array)

split <- function(array){
  mid <- as.integer(length(array)/2)
  left <- array[1:mid]
  right <- array[(mid+1):length(array)]
  return (list(left, right))
}

merge <- function(left, right){
  if(left[length(left)] < right[1]){
    return (c(left, right))
  }
  else if (right[length(right)] < left[1]){
    return (c(right, left))
  }
  left_idx = 1
  right_idx = 1
  
  result <- c()
  
  while ((left_idx <= length(left)) & (right_idx <= length(right)))
  {
    if (left[left_idx] < right[right_idx]){
      result <- c(result, left[left_idx])
      left_idx <- left_idx + 1
    }
    else {
      result <- c(result, right[right_idx])
      right_idx <- right_idx + 1
    }
  }
  
  if (left_idx <= length(left)){
    result = c(result, left[left_idx:length(left)])
  }
  else if (right_idx <= length(right)){
    result = c(result, right[right_idx:length(right)])
  }
  
  return (result)
}

mergesort <- function(array){
  if (length(array) <= 1){
    return (array)
  }
  
  left_right <- split(array)
  left <- unlist(left_right[1])
  right <- unlist(left_right[2])
  
  left <- mergesort(left)
  right <- mergesort(right)
  
  return (merge(left, right))
}