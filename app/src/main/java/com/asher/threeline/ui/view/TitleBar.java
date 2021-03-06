package com.asher.threeline.ui.view;

import android.app.Activity;
import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.text.TextUtils;
import android.util.AttributeSet;
import android.util.TypedValue;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.asher.threeline.R;

/**
 * Created by ouyangfan on 17/5/9.
 * <p>
 * titleBar
 * 沉浸式状态栏
 */
public class TitleBar extends LinearLayout {

    private int statusBarColor;
    private int titleBarColor;
    private float titleBarTitleHeight;
    private String titleBarTitle;
    private int titleBarTextColor;
    private float titleBarTextSize;
    private String leftText;
    private String rightText;
    private Drawable leftImgDrawable;
    private Drawable rightImgDrawable;

    private TextView tvLeft;
    private ImageView ivLeft;
    private TextView tvCenterTitle;
    private TextView tvRight;
    private ImageView ivRight;

    public TitleBar(Context context) {
        this(context, null);
    }

    public TitleBar(Context context, AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public TitleBar(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(context, attrs);
    }

    private void init(Context context, AttributeSet attrs) {
        //获取属性值
        TypedArray a = context.obtainStyledAttributes(attrs, R.styleable.TitleBar);
        statusBarColor = a.getColor(R.styleable.TitleBar_statusBarColor, getResources().getColor(R.color.colorPrimary));
        titleBarColor = a.getColor(R.styleable.TitleBar_titleBarColor, getResources().getColor(R.color.colorPrimaryDark));
        titleBarTitleHeight = a.getDimension(R.styleable.TitleBar_titleBarTitleHeight, getResources().getDimension(R.dimen.default_titlebar_height));
        titleBarTitle = a.getString(R.styleable.TitleBar_titleBarTitle);
        titleBarTextColor = a.getColor(R.styleable.TitleBar_titleBarTextColor, Color.WHITE);
        titleBarTextSize = a.getDimensionPixelSize(R.styleable.TitleBar_titleBarTextSize, getResources().getDimensionPixelSize(R.dimen.default_titlebar_title_size));
        leftText = a.getString(R.styleable.TitleBar_leftText);
        rightText = a.getString(R.styleable.TitleBar_rightText);
        leftImgDrawable = a.getDrawable(R.styleable.TitleBar_leftImgDrawable);
        rightImgDrawable = a.getDrawable(R.styleable.TitleBar_rightImgDrawable);
        a.recycle();

        // 设置沉浸式statusBar，以及颜色
        setFitsSystemWindows(true);
        setClipToPadding(true);
        setOrientation(VERTICAL);
        setBackgroundColor(statusBarColor);

        ViewGroup.LayoutParams title_lp = new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,
                (int) titleBarTitleHeight);

        View titleBarView = LayoutInflater.from(context).inflate(R.layout.layout_title_bar, null, false);
        titleBarView.setBackgroundColor(titleBarColor);
        tvLeft = (TextView) titleBarView.findViewById(R.id.left_text);
        ivLeft = (ImageView) titleBarView.findViewById(R.id.left_image);
        tvCenterTitle = (TextView) titleBarView.findViewById(R.id.center_text);
        tvRight = (TextView) titleBarView.findViewById(R.id.right_text);
        ivRight = (ImageView) titleBarView.findViewById(R.id.right_image);

        tvLeft.setTextColor(titleBarTextColor);
        tvRight.setTextColor(titleBarTextColor);
        tvCenterTitle.setText(titleBarTitle);
        tvCenterTitle.setTextColor(titleBarTextColor);
        tvCenterTitle.setTextSize(TypedValue.COMPLEX_UNIT_PX, titleBarTextSize);

        setTitleBar(titleBarTitle, leftText, rightText, leftImgDrawable, rightImgDrawable);
        addView(titleBarView, title_lp);
    }

    public TextView getLeftTxt() {
        return tvLeft;
    }

    public ImageView getLeftImg() {
        return ivLeft;
    }

    public TextView getTitleTxt() {
        return tvCenterTitle;
    }

    public TextView getRightTxt() {
        return tvRight;
    }

    public ImageView getRightImg() {
        return ivRight;
    }

    /**
     * 只显示标题, 没有左右图标按钮
     *
     * @param title
     */
    public void setTitleBar(String title) {
        setTitleBar(title, null, null, null, null);
    }

    /**
     * 标题加返回
     *
     * @param title
     */
    public void setTitleBarWithBack(String title) {
        Drawable leftDrawable = getResources().getDrawable(R.drawable.title_bar_left_back_selector);
        setTitleBar(title, null, null, leftDrawable, null);
    }

    public void setTitleBar(String title, Drawable leftDrawable, Drawable rightDrawable) {
        setTitleBar(title, null, null, leftDrawable, rightDrawable);
    }

    public void setTitleBar(String title, String leftText, String rightText) {
        setTitleBar(title, leftText, rightText, null, null);
    }

    /**
     * 返回按钮+右边文字
     *
     * @param title
     * @param rightText
     */
    public void setTitleBar(String title, String rightText) {
        setTitleBar(title, null, rightText, null, null);
    }

    /**
     * 返回按钮+右边图标
     *
     * @param title
     * @param rightDrawable
     */
    public void setTitleBar(String title, Drawable rightDrawable) {
        setTitleBar(title, null, null, null, rightDrawable);
    }

    /**
     * 控制标题样式
     *
     * @param title
     * @param leftTitle  左侧按钮文字 不显示为null
     * @param rightTitle 右侧按钮文字 不显示为null
     * @param leftImgRes  左侧按钮图片 不显示为null
     * @param rightImgRes 右侧按钮图片 不显示为null
     */
    public void setTitleBar(String title, String leftTitle, String rightTitle, Drawable leftImgRes, Drawable rightImgRes) {

        //左标题文字为空,则不显示
        if (TextUtils.isEmpty(leftTitle)) {
            tvLeft.setVisibility(View.GONE);
        } else {
            tvLeft.setVisibility(View.VISIBLE);
            tvLeft.setText(leftTitle);
        }

        //右标题文字为空,则不显示
        if (TextUtils.isEmpty(rightTitle)) {
            tvRight.setVisibility(View.GONE);
        } else {
            tvRight.setVisibility(View.VISIBLE);
            tvRight.setText(rightTitle);
        }

        if (leftImgRes != null) {
            ivLeft.setVisibility(View.VISIBLE);
            ivLeft.setImageDrawable(leftImgRes);
        } else {
            ivLeft.setVisibility(View.GONE);
        }

        if (rightImgRes != null) {
            ivRight.setVisibility(View.VISIBLE);
            ivRight.setImageDrawable(rightImgRes);
        } else {
            ivRight.setVisibility(View.GONE);
        }

        if (!TextUtils.isEmpty(title)) {
            tvCenterTitle.setVisibility(View.VISIBLE);
            tvCenterTitle.setText(title);
        } else {
            tvCenterTitle.setVisibility(View.GONE);
        }

    }

    /**
     * 设置左边图标的显示
     *
     * @param visibility
     */
    public void setLeftImageVisible(int visibility) {
        if (null != ivLeft) {
            ivLeft.setVisibility(visibility);
        }
    }

    /**
     * 设置右边图标的显示
     *
     * @param visibility
     */
    public void setRightImageVisible(int visibility) {
        if (null != ivRight) {
            ivRight.setVisibility(visibility);
        }
    }


    /**
     * 左部按钮点击事件
     *
     * @param listener
     */
    public void setLeftOnClickListener(View.OnClickListener listener) {
        if (tvLeft.getVisibility() == View.VISIBLE) {
            tvLeft.setOnClickListener(listener);
        } else {
            ivLeft.setOnClickListener(listener);
        }

    }

    public void setTitleTxt(String title) {
        if (!TextUtils.isEmpty(title)) {
            tvCenterTitle.setVisibility(View.VISIBLE);
            tvCenterTitle.setText(title);
        } else {
            tvCenterTitle.setVisibility(View.GONE);
        }
    }


    /**
     * 右部按钮点击事件
     *
     * @param listener
     */
    public void setRightOnClickListener(View.OnClickListener listener) {
        if (tvRight.getVisibility() == View.VISIBLE) {
            tvRight.setOnClickListener(listener);
        } else {
            ivRight.setOnClickListener(listener);
        }
    }

    /**
     * 标题点击事件
     *
     * @param listener
     */
    public void setCenterOnClickListener(View.OnClickListener listener) {
        if (tvCenterTitle.getVisibility() == View.VISIBLE) {
            tvCenterTitle.setOnClickListener(listener);
        }
    }

    public static int getStatusBarHeight(Context context) {
        int result = 0;
        int resourceId = context.getResources().getIdentifier("status_bar_height", "dimen", "android");
        if (resourceId > 0) {
            result = context.getResources().getDimensionPixelSize(resourceId);
        }
        return result;
    }

    public static TitleBar getInstance(Activity context) {
        return (TitleBar) ((ViewGroup) context.findViewById(android.R.id.content)).getChildAt(0);
    }
}
