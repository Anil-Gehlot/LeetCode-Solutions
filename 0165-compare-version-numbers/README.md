<h2><a href="https://leetcode.com/problems/compare-version-numbers/">165. Compare Version Numbers</a></h2><h3>Medium</h3><hr><div><p>Given two <strong>version strings</strong>,&nbsp;<code>version1</code> and <code>version2</code>, compare them. A version string consists of <strong>revisions</strong> separated by dots <code>'.'</code>. The <strong>value of the revision</strong> is its <strong>integer conversion</strong> ignoring leading zeros.</p>

<p>To compare version strings, compare their revision values in <strong>left-to-right order</strong>. If one of the version strings has fewer revisions, treat the missing revision values as <code>0</code>.</p>

<p><em>Return the following:</em></p>

<ul>
	<li>If <code>version1 &lt; version2</code>, return <code>-1</code>.</li>
	<li>If <code>version1 &gt; version2</code>, return <code>1</code>.</li>
	<li>Otherwise, return <code>0</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">version1 = "1.2", version2 = "1.10"</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>version1's second revision is "2" and version2's second revision is "10": 2 &lt; 10, so version1 &lt; version2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">version1 = "1.01", version2 = "1.001"</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Ignoring leading zeroes, both "01" and "001" represent the same integer "1".</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">version1 = "1.0", version2 = "1.0.0.0"</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>version1 has less revisions, which means every missing revision are treated as "0".</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= version1.length, version2.length &lt;= 500</code></li>
	<li><code>version1</code> and <code>version2</code>&nbsp;only contain digits and <code>'.'</code>.</li>
	<li><code>version1</code> and <code>version2</code>&nbsp;<strong>are valid version numbers</strong>.</li>
	<li>All the given revisions in&nbsp;<code>version1</code> and <code>version2</code>&nbsp;can be stored in&nbsp;a&nbsp;<strong>32-bit integer</strong>.</li>
</ul>
</div>