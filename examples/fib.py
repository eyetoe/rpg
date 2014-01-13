<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  
  


  

  <head>
    <title>
      /examples/fib.py – Urwid
    </title>
        <link rel="search" href="/urwid/search" />
        <link rel="help" href="/urwid/wiki/TracGuide" />
        <link rel="alternate" href="/urwid/browser/examples/fib.py?format=txt" type="text/plain" title="Plain Text" /><link rel="alternate" href="/urwid/export/984%3Ad6071ec65299/examples/fib.py" type="text/x-python; charset=utf-8" title="Original Format" />
        <link rel="up" href="/urwid/browser/examples" title="Parent directory" />
        <link rel="start" href="/urwid/wiki" />
        <link rel="stylesheet" href="/urwid/chrome/common/css/trac.css" type="text/css" /><link rel="stylesheet" href="/urwid/chrome/common/css/code.css" type="text/css" /><link rel="stylesheet" href="/urwid/pygments/trac.css" type="text/css" /><link rel="stylesheet" href="/urwid/chrome/common/css/browser.css" type="text/css" />
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
        <link rel="icon" href="/favicon.ico" type="image/x-icon" />
      <link type="application/opensearchdescription+xml" rel="search" href="/urwid/search/opensearch" title="Search Urwid" />
    <script type="text/javascript" src="/urwid/chrome/common/js/jquery.js"></script><script type="text/javascript" src="/urwid/chrome/common/js/trac.js"></script><script type="text/javascript" src="/urwid/chrome/common/js/search.js"></script>
    <!--[if lt IE 7]>
    <script type="text/javascript" src="/urwid/chrome/common/js/ie_pre7_hacks.js"></script>
    <![endif]-->
    <script type="text/javascript">
      jQuery(document).ready(function($) {
        $("#jumploc input").hide();
        $("#jumploc select").change(function () {
          this.parentNode.parentNode.submit();
        })
      });
    </script>
  </head>
  <body>
    <div id="banner">
      <div id="header">
        <a id="logo" href="http://excess.org/urwid/"><img src="/urwid/info001.png" alt="Urwid" height="50" width="150" /></a>
      </div>
      <form id="search" action="/urwid/search" method="get">
        <div>
          <label for="proj-search">Search:</label>
          <input type="text" id="proj-search" name="q" size="18" value="" />
          <input type="submit" value="Search" />
        </div>
      </form>
      <div id="metanav" class="nav">
    <ul>
      <li class="first"><a href="/urwid/login">Login</a></li><li><a href="/urwid/wiki/TracGuide">Help/Guide</a></li><li><a href="/urwid/about">About Trac</a></li><li><a href="/urwid/prefs">Preferences</a></li><li class="last"><a href="/urwid/register">Register</a></li>
    </ul>
  </div>
    </div>
    <div id="mainnav" class="nav">
    <ul>
      <li class="first"><a href="/urwid/wiki">Wiki</a></li><li><a href="/urwid/timeline">Timeline</a></li><li><a href="/urwid/roadmap">Roadmap</a></li><li class="active"><a href="/urwid/browser">Browse Source</a></li><li><a href="/urwid/report">View Tickets</a></li><li class="last"><a href="/urwid/search">Search</a></li>
    </ul>
  </div>
    <div id="main">
      <div id="ctxtnav" class="nav">
        <h2>Context Navigation</h2>
          <ul>
              <li class="first"><a href="/urwid/changeset/661%3A24cf14eac74f/examples/fib.py">Last Change</a></li><li><a href="/urwid/browser/examples/fib.py?annotate=blame&amp;rev=661%3A24cf14eac74f" title="Annotate each line with the last changed revision (this can be time consuming...)">Annotate</a></li><li class="last"><a href="/urwid/log/examples/fib.py">Revision Log</a></li>
          </ul>
        <hr />
      </div>
    <div id="content" class="browser">
      <h1>
    <a class="pathentry first" title="Go to root directory" href="/urwid/browser">root</a><span class="pathentry sep">/</span><a class="pathentry" title="View examples" href="/urwid/browser/examples">examples</a><span class="pathentry sep">/</span><a class="pathentry" title="View fib.py" href="/urwid/browser/examples/fib.py">fib.py</a>
    <br style="clear: both" />
  </h1>
      <div id="jumprev">
        <form action="" method="get">
          <div>
            <label for="rev">
              View revision:</label>
            <input type="text" id="rev" name="rev" size="6" />
          </div>
        </form>
      </div>
      <div id="jumploc">
        <form action="" method="get">
          <div class="buttons">
            <label for="preselected">Visit:</label>
            <select id="preselected" name="preselected">
              <option selected="selected"></option>
              <optgroup label="branches">
                <option value="/urwid/browser/?rev=984%3Ad6071ec65299">default</option><option value="/urwid/browser/?rev=983%3Afb12872964c0">stable-1.1</option><option value="/urwid/browser/?rev=967%3A8d8ab02fb23f">stable-1.0</option><option value="/urwid/browser/?rev=906%3A4c76eaf52f56">feature-containers</option><option value="/urwid/browser/?rev=905%3A992684bb8aaf">feature-sphinx</option><option value="/urwid/browser/?rev=658%3Ab451e1bce91f">stable-0.9.9</option><option value="/urwid/browser/?rev=547%3Aa7bbf31723ec">python3</option><option value="/urwid/browser/?rev=516%3A6a50ee98e121">idle</option><option value="/urwid/browser/?rev=515%3Ad3ee5a3dda3c">glib</option>
              </optgroup><optgroup label="tags">
                <option value="/urwid/browser/?rev=984%3Ad6071ec65299">tip</option><option value="/urwid/browser/?rev=968%3A0b6e52fa478a">release-1.1.1</option><option value="/urwid/browser/?rev=965%3Ad6ac41030748">release-1.0.3</option><option value="/urwid/browser/?rev=954%3A19012001f152">release-1.1.0</option><option value="/urwid/browser/?rev=818%3A0dbd86bab1f2">release-1.0.2</option><option value="/urwid/browser/?rev=656%3A0b46d54a527e">release-1.0.1</option><option value="/urwid/browser/?rev=641%3A0cb6dd176164">release-0.9.9.3</option><option value="/urwid/browser/?rev=615%3A36a3475de956">release-1.0.0</option><option value="/urwid/browser/?rev=576%3A4701bc9ea3f1">release-0.9.9.2</option><option value="/urwid/browser/?rev=305%3Af445b883a200">release-0.9.9.1</option><option value="/urwid/browser/?rev=292%3A167d78b81824">release-0.9.9</option><option value="/urwid/browser/?rev=65%3Af71120f89f4a">release-0.9.8</option><option value="/urwid/browser/?rev=26%3A80fb799e57f6">release-0.9.7.2</option><option value="/urwid/browser/?rev=23%3A6940f8e182d1">release-0.9.7.1</option><option value="/urwid/browser/?rev=22%3A51ae19b2d071">release-0.9.7</option><option value="/urwid/browser/?rev=21%3Ae985496ab59f">release-0.9.6</option><option value="/urwid/browser/?rev=20%3A724fa210dbd7">release-0.9.5</option><option value="/urwid/browser/?rev=19%3A55a4dbaf0f4c">release-0.9.4</option><option value="/urwid/browser/?rev=18%3A3e41e992e58d">release-0.9.3</option><option value="/urwid/browser/?rev=17%3A77fad9b941bd">release-0.9.2</option><option value="/urwid/browser/?rev=16%3Af523745d15d4">release-0.9.1</option><option value="/urwid/browser/?rev=15%3A00ecfc18e7a3">release-0.9.0</option><option value="/urwid/browser/?rev=14%3A4d54f0d3d092">release-0.9.0-pre3</option><option value="/urwid/browser/?rev=13%3Aa32c3d617c3c">release-0.9.0-pre2</option><option value="/urwid/browser/?rev=12%3Ad8ccab6cab52">release-0.9.0-pre1</option><option value="/urwid/browser/?rev=11%3A75e410b77de0">release-0.8.10</option><option value="/urwid/browser/?rev=10%3Ab08a823827c3">release-0.8.9</option><option value="/urwid/browser/?rev=9%3A9488661c4e88">release-0.8.8</option><option value="/urwid/browser/?rev=8%3A20d334bf7f99">release-0.8.7</option><option value="/urwid/browser/?rev=7%3A4a94ee84f10a">release-0.8.6</option><option value="/urwid/browser/?rev=6%3A0836e10d9971">release-0.8.5</option><option value="/urwid/browser/?rev=5%3A9fc455b9845b">release-0.8.4</option><option value="/urwid/browser/?rev=4%3Abac46c2f4010">release-0.8.3</option><option value="/urwid/browser/?rev=3%3Aea35d3af1d66">release-0.8.2</option><option value="/urwid/browser/?rev=2%3A8635df78aaf5">release-0.8.1</option><option value="/urwid/browser/?rev=1%3A77ca4911a81a">release-0.8.0</option>
              </optgroup>
            </select>
            <input type="submit" value="Go!" title="Jump to the chosen preselected path" />
          </div>
        </form>
      </div>
      <table id="info" summary="Revision info">
        <tr>
          <th scope="col">
            Revision <a href="/urwid/changeset/661%3A24cf14eac74f">661:24cf14eac74f</a>, <span title="3665 bytes">3.6 KB</span>
            (checked in by Ian Ward &lt;ian@…&gt;, <a class="timeline" href="/urwid/timeline?from=2011-11-29T00%3A20%3A13-0500&amp;precision=second" title="2011-11-29T00:20:13-0500 in Timeline">2 years</a> ago)
          </th>
        </tr>
        <tr>
          <td class="message searchable">
              <p>
move examples to examples/<br />
</p>
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <ul class="props">
              <li>
                  Property <strong>exe</strong> set to
                    <em><code>*</code></em>
              </li>
            </ul>
          </td>
        </tr>
      </table>
      <div id="preview" class="searchable">
    <table class="code"><thead><tr><th class="lineno" title="Line numbers">Line</th><th class="content"> </th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th><td><span class="c">#!/usr/bin/python</span></td></tr><tr><th id="L2"><a href="#L2">2</a></th><td><span class="c">#</span></td></tr><tr><th id="L3"><a href="#L3">3</a></th><td><span class="c"># Urwid example fibonacci sequence viewer / unbounded data demo</span></td></tr><tr><th id="L4"><a href="#L4">4</a></th><td><span class="c">#    Copyright (C) 2004-2007  Ian Ward</span></td></tr><tr><th id="L5"><a href="#L5">5</a></th><td><span class="c">#</span></td></tr><tr><th id="L6"><a href="#L6">6</a></th><td><span class="c">#    This library is free software; you can redistribute it and/or</span></td></tr><tr><th id="L7"><a href="#L7">7</a></th><td><span class="c">#    modify it under the terms of the GNU Lesser General Public</span></td></tr><tr><th id="L8"><a href="#L8">8</a></th><td><span class="c">#    License as published by the Free Software Foundation; either</span></td></tr><tr><th id="L9"><a href="#L9">9</a></th><td><span class="c">#    version 2.1 of the License, or (at your option) any later version.</span></td></tr><tr><th id="L10"><a href="#L10">10</a></th><td><span class="c">#</span></td></tr><tr><th id="L11"><a href="#L11">11</a></th><td><span class="c">#    This library is distributed in the hope that it will be useful,</span></td></tr><tr><th id="L12"><a href="#L12">12</a></th><td><span class="c">#    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></td></tr><tr><th id="L13"><a href="#L13">13</a></th><td><span class="c">#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU</span></td></tr><tr><th id="L14"><a href="#L14">14</a></th><td><span class="c">#    Lesser General Public License for more details.</span></td></tr><tr><th id="L15"><a href="#L15">15</a></th><td><span class="c">#</span></td></tr><tr><th id="L16"><a href="#L16">16</a></th><td><span class="c">#    You should have received a copy of the GNU Lesser General Public</span></td></tr><tr><th id="L17"><a href="#L17">17</a></th><td><span class="c">#    License along with this library; if not, write to the Free Software</span></td></tr><tr><th id="L18"><a href="#L18">18</a></th><td><span class="c">#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA</span></td></tr><tr><th id="L19"><a href="#L19">19</a></th><td><span class="c">#</span></td></tr><tr><th id="L20"><a href="#L20">20</a></th><td><span class="c"># Urwid web site: http://excess.org/urwid/</span></td></tr><tr><th id="L21"><a href="#L21">21</a></th><td></td></tr><tr><th id="L22"><a href="#L22">22</a></th><td><span class="sd">"""</span></td></tr><tr><th id="L23"><a href="#L23">23</a></th><td><span class="sd">Urwid example fibonacci sequence viewer / unbounded data demo</span></td></tr><tr><th id="L24"><a href="#L24">24</a></th><td><span class="sd"></span></td></tr><tr><th id="L25"><a href="#L25">25</a></th><td><span class="sd">Features:</span></td></tr><tr><th id="L26"><a href="#L26">26</a></th><td><span class="sd">- custom list walker class for browsing infinite set</span></td></tr><tr><th id="L27"><a href="#L27">27</a></th><td><span class="sd">- custom wrap mode "numeric" for wrapping numbers to right and bottom</span></td></tr><tr><th id="L28"><a href="#L28">28</a></th><td><span class="sd">"""</span></td></tr><tr><th id="L29"><a href="#L29">29</a></th><td></td></tr><tr><th id="L30"><a href="#L30">30</a></th><td><span class="k">import</span> <span class="nn">urwid</span></td></tr><tr><th id="L31"><a href="#L31">31</a></th><td>        </td></tr><tr><th id="L32"><a href="#L32">32</a></th><td><span class="k">class</span> <span class="nc">FibonacciWalker</span><span class="p">(</span>urwid<span class="o">.</span>ListWalker<span class="p">):</span></td></tr><tr><th id="L33"><a href="#L33">33</a></th><td>    <span class="sd">"""ListWalker-compatible class for browsing fibonacci set.</span></td></tr><tr><th id="L34"><a href="#L34">34</a></th><td><span class="sd">    </span></td></tr><tr><th id="L35"><a href="#L35">35</a></th><td><span class="sd">    positions returned are (value at position-1, value at poistion) tuples.</span></td></tr><tr><th id="L36"><a href="#L36">36</a></th><td><span class="sd">    """</span></td></tr><tr><th id="L37"><a href="#L37">37</a></th><td>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></td></tr><tr><th id="L38"><a href="#L38">38</a></th><td>        <span class="bp">self</span><span class="o">.</span>focus <span class="o">=</span> <span class="p">(</span><span class="mf">0</span>L<span class="p">,</span><span class="mf">1</span>L<span class="p">)</span></td></tr><tr><th id="L39"><a href="#L39">39</a></th><td>        <span class="bp">self</span><span class="o">.</span>numeric_layout <span class="o">=</span> NumericLayout<span class="p">()</span></td></tr><tr><th id="L40"><a href="#L40">40</a></th><td>    </td></tr><tr><th id="L41"><a href="#L41">41</a></th><td>    <span class="k">def</span> <span class="nf">_get_at_pos</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> pos<span class="p">):</span></td></tr><tr><th id="L42"><a href="#L42">42</a></th><td>        <span class="sd">"""Return a widget and the position passed."""</span></td></tr><tr><th id="L43"><a href="#L43">43</a></th><td>        <span class="k">return</span> urwid<span class="o">.</span>Text<span class="p">(</span><span class="s">"</span><span class="si">%d</span><span class="s">"</span><span class="o">%</span>pos<span class="p">[</span><span class="mf">1</span><span class="p">],</span> layout<span class="o">=</span><span class="bp">self</span><span class="o">.</span>numeric_layout<span class="p">),</span> pos</td></tr><tr><th id="L44"><a href="#L44">44</a></th><td>    </td></tr><tr><th id="L45"><a href="#L45">45</a></th><td>    <span class="k">def</span> <span class="nf">get_focus</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> </td></tr><tr><th id="L46"><a href="#L46">46</a></th><td>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span>_get_at_pos<span class="p">(</span><span class="bp">self</span><span class="o">.</span>focus<span class="p">)</span></td></tr><tr><th id="L47"><a href="#L47">47</a></th><td>    </td></tr><tr><th id="L48"><a href="#L48">48</a></th><td>    <span class="k">def</span> <span class="nf">set_focus</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> focus<span class="p">):</span></td></tr><tr><th id="L49"><a href="#L49">49</a></th><td>        <span class="bp">self</span><span class="o">.</span>focus <span class="o">=</span> focus</td></tr><tr><th id="L50"><a href="#L50">50</a></th><td>        <span class="bp">self</span><span class="o">.</span>_modified<span class="p">()</span></td></tr><tr><th id="L51"><a href="#L51">51</a></th><td>    </td></tr><tr><th id="L52"><a href="#L52">52</a></th><td>    <span class="k">def</span> <span class="nf">get_next</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> start_from<span class="p">):</span></td></tr><tr><th id="L53"><a href="#L53">53</a></th><td>        a<span class="p">,</span> b <span class="o">=</span> start_from</td></tr><tr><th id="L54"><a href="#L54">54</a></th><td>        focus <span class="o">=</span> b<span class="p">,</span> a<span class="o">+</span>b</td></tr><tr><th id="L55"><a href="#L55">55</a></th><td>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span>_get_at_pos<span class="p">(</span>focus<span class="p">)</span></td></tr><tr><th id="L56"><a href="#L56">56</a></th><td>    </td></tr><tr><th id="L57"><a href="#L57">57</a></th><td>    <span class="k">def</span> <span class="nf">get_prev</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> start_from<span class="p">):</span></td></tr><tr><th id="L58"><a href="#L58">58</a></th><td>        a<span class="p">,</span> b <span class="o">=</span> start_from</td></tr><tr><th id="L59"><a href="#L59">59</a></th><td>        focus <span class="o">=</span> b<span class="o">-</span>a<span class="p">,</span> a</td></tr><tr><th id="L60"><a href="#L60">60</a></th><td>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span>_get_at_pos<span class="p">(</span>focus<span class="p">)</span></td></tr><tr><th id="L61"><a href="#L61">61</a></th><td></td></tr><tr><th id="L62"><a href="#L62">62</a></th><td><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></td></tr><tr><th id="L63"><a href="#L63">63</a></th><td>    palette <span class="o">=</span> <span class="p">[</span></td></tr><tr><th id="L64"><a href="#L64">64</a></th><td>        <span class="p">(</span><span class="s">'body'</span><span class="p">,</span><span class="s">'black'</span><span class="p">,</span><span class="s">'dark cyan'</span><span class="p">,</span> <span class="s">'standout'</span><span class="p">),</span></td></tr><tr><th id="L65"><a href="#L65">65</a></th><td>        <span class="p">(</span><span class="s">'foot'</span><span class="p">,</span><span class="s">'light gray'</span><span class="p">,</span> <span class="s">'black'</span><span class="p">),</span></td></tr><tr><th id="L66"><a href="#L66">66</a></th><td>        <span class="p">(</span><span class="s">'key'</span><span class="p">,</span><span class="s">'light cyan'</span><span class="p">,</span> <span class="s">'black'</span><span class="p">,</span> <span class="s">'underline'</span><span class="p">),</span></td></tr><tr><th id="L67"><a href="#L67">67</a></th><td>        <span class="p">(</span><span class="s">'title'</span><span class="p">,</span> <span class="s">'white'</span><span class="p">,</span> <span class="s">'black'</span><span class="p">,),</span></td></tr><tr><th id="L68"><a href="#L68">68</a></th><td>        <span class="p">]</span></td></tr><tr><th id="L69"><a href="#L69">69</a></th><td>        </td></tr><tr><th id="L70"><a href="#L70">70</a></th><td>    footer_text <span class="o">=</span> <span class="p">[</span></td></tr><tr><th id="L71"><a href="#L71">71</a></th><td>        <span class="p">(</span><span class="s">'title'</span><span class="p">,</span> <span class="s">"Fibonacci Set Viewer"</span><span class="p">),</span> <span class="s">"    "</span><span class="p">,</span></td></tr><tr><th id="L72"><a href="#L72">72</a></th><td>        <span class="p">(</span><span class="s">'key'</span><span class="p">,</span> <span class="s">"UP"</span><span class="p">),</span> <span class="s">", "</span><span class="p">,</span> <span class="p">(</span><span class="s">'key'</span><span class="p">,</span> <span class="s">"DOWN"</span><span class="p">),</span> <span class="s">", "</span><span class="p">,</span></td></tr><tr><th id="L73"><a href="#L73">73</a></th><td>        <span class="p">(</span><span class="s">'key'</span><span class="p">,</span> <span class="s">"PAGE UP"</span><span class="p">),</span> <span class="s">" and "</span><span class="p">,</span> <span class="p">(</span><span class="s">'key'</span><span class="p">,</span> <span class="s">"PAGE DOWN"</span><span class="p">),</span></td></tr><tr><th id="L74"><a href="#L74">74</a></th><td>        <span class="s">" move view  "</span><span class="p">,</span></td></tr><tr><th id="L75"><a href="#L75">75</a></th><td>        <span class="p">(</span><span class="s">'key'</span><span class="p">,</span> <span class="s">"Q"</span><span class="p">),</span> <span class="s">" exits"</span><span class="p">,</span></td></tr><tr><th id="L76"><a href="#L76">76</a></th><td>        <span class="p">]</span></td></tr><tr><th id="L77"><a href="#L77">77</a></th><td>    </td></tr><tr><th id="L78"><a href="#L78">78</a></th><td>    <span class="k">def</span> <span class="nf">exit_on_q</span><span class="p">(</span><span class="nb">input</span><span class="p">):</span></td></tr><tr><th id="L79"><a href="#L79">79</a></th><td>        <span class="k">if</span> <span class="nb">input</span> <span class="ow">in</span> <span class="p">(</span><span class="s">'q'</span><span class="p">,</span> <span class="s">'Q'</span><span class="p">):</span></td></tr><tr><th id="L80"><a href="#L80">80</a></th><td>            <span class="k">raise</span> urwid<span class="o">.</span>ExitMainLoop<span class="p">()</span></td></tr><tr><th id="L81"><a href="#L81">81</a></th><td></td></tr><tr><th id="L82"><a href="#L82">82</a></th><td>    listbox <span class="o">=</span> urwid<span class="o">.</span>ListBox<span class="p">(</span>FibonacciWalker<span class="p">())</span></td></tr><tr><th id="L83"><a href="#L83">83</a></th><td>    footer <span class="o">=</span> urwid<span class="o">.</span>AttrMap<span class="p">(</span>urwid<span class="o">.</span>Text<span class="p">(</span>footer_text<span class="p">),</span> <span class="s">'foot'</span><span class="p">)</span></td></tr><tr><th id="L84"><a href="#L84">84</a></th><td>    view <span class="o">=</span> urwid<span class="o">.</span>Frame<span class="p">(</span>urwid<span class="o">.</span>AttrWrap<span class="p">(</span>listbox<span class="p">,</span> <span class="s">'body'</span><span class="p">),</span> footer<span class="o">=</span>footer<span class="p">)</span></td></tr><tr><th id="L85"><a href="#L85">85</a></th><td>    loop <span class="o">=</span> urwid<span class="o">.</span>MainLoop<span class="p">(</span>view<span class="p">,</span> palette<span class="p">,</span> unhandled_input<span class="o">=</span>exit_on_q<span class="p">)</span></td></tr><tr><th id="L86"><a href="#L86">86</a></th><td>    loop<span class="o">.</span>run<span class="p">()</span></td></tr><tr><th id="L87"><a href="#L87">87</a></th><td></td></tr><tr><th id="L88"><a href="#L88">88</a></th><td></td></tr><tr><th id="L89"><a href="#L89">89</a></th><td><span class="k">class</span> <span class="nc">NumericLayout</span><span class="p">(</span>urwid<span class="o">.</span>TextLayout<span class="p">):</span></td></tr><tr><th id="L90"><a href="#L90">90</a></th><td>    <span class="sd">"""</span></td></tr><tr><th id="L91"><a href="#L91">91</a></th><td><span class="sd">    TextLayout class for bottom-right aligned numbers</span></td></tr><tr><th id="L92"><a href="#L92">92</a></th><td><span class="sd">    """</span></td></tr><tr><th id="L93"><a href="#L93">93</a></th><td>    <span class="k">def</span> <span class="nf">layout</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> text<span class="p">,</span> width<span class="p">,</span> align<span class="p">,</span> wrap <span class="p">):</span></td></tr><tr><th id="L94"><a href="#L94">94</a></th><td>        <span class="sd">"""</span></td></tr><tr><th id="L95"><a href="#L95">95</a></th><td><span class="sd">        Return layout structure for right justified numbers.</span></td></tr><tr><th id="L96"><a href="#L96">96</a></th><td><span class="sd">        """</span></td></tr><tr><th id="L97"><a href="#L97">97</a></th><td>        lt <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>text<span class="p">)</span></td></tr><tr><th id="L98"><a href="#L98">98</a></th><td>        r <span class="o">=</span> lt <span class="o">%</span> width <span class="c"># remaining segment not full width wide</span></td></tr><tr><th id="L99"><a href="#L99">99</a></th><td>        <span class="k">if</span> r<span class="p">:</span></td></tr><tr><th id="L100"><a href="#L100">100</a></th><td>            linestarts <span class="o">=</span> <span class="nb">range</span><span class="p">(</span> r<span class="p">,</span> lt<span class="p">,</span> width <span class="p">)</span></td></tr><tr><th id="L101"><a href="#L101">101</a></th><td>            <span class="k">return</span> <span class="p">[</span></td></tr><tr><th id="L102"><a href="#L102">102</a></th><td>                <span class="c"># right-align the remaining segment on 1st line</span></td></tr><tr><th id="L103"><a href="#L103">103</a></th><td>                <span class="p">[(</span>width<span class="o">-</span>r<span class="p">,</span><span class="bp">None</span><span class="p">),(</span>r<span class="p">,</span> <span class="mf">0</span><span class="p">,</span> r<span class="p">)]</span></td></tr><tr><th id="L104"><a href="#L104">104</a></th><td>                <span class="c"># fill the rest of the lines</span></td></tr><tr><th id="L105"><a href="#L105">105</a></th><td>                <span class="p">]</span> <span class="o">+</span> <span class="p">[[(</span>width<span class="p">,</span> x<span class="p">,</span> x<span class="o">+</span>width<span class="p">)]</span> <span class="k">for</span> x <span class="ow">in</span> linestarts<span class="p">]</span></td></tr><tr><th id="L106"><a href="#L106">106</a></th><td>        <span class="k">else</span><span class="p">:</span></td></tr><tr><th id="L107"><a href="#L107">107</a></th><td>            linestarts <span class="o">=</span> <span class="nb">range</span><span class="p">(</span> <span class="mf">0</span><span class="p">,</span> lt<span class="p">,</span> width <span class="p">)</span></td></tr><tr><th id="L108"><a href="#L108">108</a></th><td>            <span class="k">return</span> <span class="p">[[(</span>width<span class="p">,</span> x<span class="p">,</span> x<span class="o">+</span>width<span class="p">)]</span> <span class="k">for</span> x <span class="ow">in</span> linestarts<span class="p">]</span></td></tr><tr><th id="L109"><a href="#L109">109</a></th><td></td></tr><tr><th id="L110"><a href="#L110">110</a></th><td></td></tr><tr><th id="L111"><a href="#L111">111</a></th><td><span class="k">if</span> __name__<span class="o">==</span><span class="s">"__main__"</span><span class="p">:</span> </td></tr><tr><th id="L112"><a href="#L112">112</a></th><td>    main<span class="p">()</span></td></tr></tbody></table>
      </div>
      <div id="help">
        <strong>Note:</strong> See <a href="/urwid/wiki/TracBrowser">TracBrowser</a>
        for help on using the browser.
      </div>
      <div id="anydiff">
        <form action="/urwid/diff" method="get">
          <div class="buttons">
            <input type="hidden" name="new_path" value="/examples/fib.py" />
            <input type="hidden" name="old_path" value="/examples/fib.py" />
            <input type="hidden" name="new_rev" value="661:24cf14eac74f" />
            <input type="hidden" name="old_rev" value="661:24cf14eac74f" />
            <input type="submit" value="View changes..." title="Select paths and revs for Diff" />
          </div>
        </form>
      </div>
    </div>
    <div id="altlinks">
      <h3>Download in other formats:</h3>
      <ul>
        <li class="first">
          <a rel="nofollow" href="/urwid/browser/examples/fib.py?format=txt">Plain Text</a>
        </li><li class="last">
          <a rel="nofollow" href="/urwid/export/984%3Ad6071ec65299/examples/fib.py">Original Format</a>
        </li>
      </ul>
    </div>
    </div>
    <div id="footer" lang="en" xml:lang="en"><hr />
      <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/urwid/chrome/common/trac_logo_mini.png" height="30" width="107" alt="Trac Powered" /></a>
      <p class="left">
        Powered by <a href="/urwid/about"><strong>Trac 0.11.3</strong></a><br />
        By <a href="http://www.edgewall.org/">Edgewall Software</a>.
      </p>
      <p class="right"><a href="http://excess.org/urwid/">Urwid</a> - Console User Interface Library for Python</p>
    </div>
  </body>
</html>