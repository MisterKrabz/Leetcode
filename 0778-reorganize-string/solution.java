class Solution {
    public String reorganizeString(String s) {
        // store each character in the string inside of a bucket style array; a = 0, z = 25
        // first, enter the most frequent character at the start of the output array 
        // next, place the next most frequent character in the start of the output array 
        // continue until each bucket contains the same number of characters, excluding the zero buckets 
        // finally, traverse the buckets array and continue putting eacch element into each position within the buckets array 

        // the buckets for the characters 
        int [] buckets = new int[26];

        // populate the buckets with data 
        for(int i = 0; i < s.length(); i++){
            buckets[s.charAt(i) - 'a'] ++;
        }
        
        int [] output = new int[s.length()];
        // place each character in the final array 
        int outputIndex = 0;
        for(int i = 0; i < buckets.length; i++){
            int max = 0;
            char maxChar = 'a';
            int maxIndex = 0;

            for(int j = 0; j < buckets.length; j++){
                if(buckets[j] > max){
                    max = buckets[j];
                    maxChar = (char)(j + 'a');
                    maxIndex = j;
                }
            }

            while(max != 0){
                output[outputIndex] = maxChar;
                // start by populating even indexes 
                outputIndex += 2;

                // when it reaches the end of the array then we will start populating the odd indexes 
                if(outputIndex >= output.length){
                    outputIndex = 1;
                }
                max--;
            }

            buckets[maxIndex] = 0;
        }


        String str = "";
        int prev = -1;
        for(int i = 0; i < output.length; i++){
            if(prev == output[i]) {
                return "";
            }
            str = str + (char)output[i];
            prev = output[i];
        }

        return str;
    }
}
