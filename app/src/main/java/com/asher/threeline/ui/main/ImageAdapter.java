package com.asher.threeline.ui.main;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.asher.threeline.R;
import com.asher.threeline.db.IType;
import com.asher.threeline.db.bean.DbContent;

import java.util.List;

public class ImageAdapter extends BaseAdapter {

    private static final String TAG = "ImageAdapter";

    private LayoutInflater mInflater;
    private List<DbContent> mDbContentList;
    private final int TYPE_COUNT = 4;

    public ImageAdapter(Context context, List<DbContent> dbContents) {
        mInflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        mDbContentList = dbContents;
    }

    @Override
    public int getCount() {
        Log.i(TAG, "size = " + mDbContentList.size());
        return null == mDbContentList ? 0 : mDbContentList.size();
    }

    @Override
    public Object getItem(int position) {
        return position;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public int getItemViewType(int position) {
        if (null == mDbContentList || mDbContentList.isEmpty()) {
            return super.getItemViewType(position);
        }
        return mDbContentList.get(position).getType() == null ? IType.TYPE_INVALID :
                mDbContentList.get(position).getType();
    }

    @Override
    public int getViewTypeCount() {
        return TYPE_COUNT;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        DbContent dbContent = mDbContentList.get(position);
        int currentType = getItemViewType(position);
        Log.i(TAG, "currentType = " + currentType + " , dbContent = " + dbContent);
        if (null == convertView) {
            switch (currentType) {
                case IType.TYPE_ARTICLE:
                    return recycleArticleViewHolder(dbContent, convertView, parent);
                case IType.TYPE_SENTENCE:
                    return recycleSentenceViewHolder(dbContent, convertView, parent);
                case IType.TYPE_MUSIC:
                    return recycleMusicViewHolder(dbContent, convertView, parent);
                case IType.TYPE_IMAGE:
                    return recycleImageViewHolder(dbContent, convertView, parent);
                default:
                    return recycleImageViewHolder(dbContent, convertView, parent);
            }
        }
        return convertView;
    }

    /**
     * recycler view holder
     *
     * @param dbContent
     * @param convertView
     * @param parent
     */
    private View recycleArticleViewHolder(DbContent dbContent, View convertView,
                                          ViewGroup parent) {
        ArticleViewHolder articleViewHolder = null;
        // 第一次没有加载convertView
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_article_item, parent, false);
            articleViewHolder = new ArticleViewHolder(convertView);
            convertView.setTag(articleViewHolder);
        } else {
            articleViewHolder = (ArticleViewHolder) convertView.getTag();
        }
        setArticleData(dbContent, articleViewHolder);
       return convertView;
    }

    private View recycleSentenceViewHolder(DbContent dbContent, View convertView,
                                           ViewGroup parent) {
        SentenceViewHolder sentenceViewHolder = null;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_sentence_item, parent, false);
            sentenceViewHolder = new SentenceViewHolder(convertView);
            convertView.setTag(sentenceViewHolder);
        } else {
            sentenceViewHolder = (SentenceViewHolder) convertView.getTag();
        }
        setSentenceData(dbContent, sentenceViewHolder);
        return convertView;
    }

    private View recycleMusicViewHolder(DbContent dbContent, View convertView,
                                        ViewGroup parent) {
        MusicViewHolder musicViewHolder = null;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_music_item, parent, false);
            musicViewHolder = new MusicViewHolder(convertView);
            convertView.setTag(musicViewHolder);
        } else {
            musicViewHolder = (MusicViewHolder) convertView.getTag();
        }
        setMusicData(dbContent, musicViewHolder);
        return convertView;
    }

    private View recycleImageViewHolder(DbContent dbContent, View convertView,
                                        ViewGroup parent) {
        ImageViewHolder imageViewHolder = null;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_image_item, parent, false);
            imageViewHolder = new ImageViewHolder(convertView);
            convertView.setTag(imageViewHolder);
        } else {
            imageViewHolder = (ImageViewHolder) convertView.getTag();
        }
        setImageData(dbContent, imageViewHolder);
        return convertView;
    }

    /**
     * set article data
     *
     * @param article    data
     * @param viewHolder holder
     */
    private void setArticleData(DbContent article, ArticleViewHolder viewHolder) {
        viewHolder.articleTitle.setText(article.getTitle());
        viewHolder.articleAuthor.setText(article.getAuthor());
        Log.i(TAG, "setArticleData article = " + article);
    }

    private void setSentenceData(DbContent sentence, SentenceViewHolder viewHolder) {
        viewHolder.sentenceContent.setText(sentence.getContent());
        Log.i(TAG, "setSentenceData sentence = " + sentence);
    }

    private void setMusicData(DbContent music, MusicViewHolder viewHolder) {
        viewHolder.musicAuthor.setText(music.getAuthor());
        viewHolder.musicTitle.setText(music.getTitle());
//        viewHolder.musicCover.setImageResource(music.getImagePath());
        Log.i(TAG, "setMusicData music = " + music);
    }

    private void setImageData(DbContent image, ImageViewHolder viewHolder) {
//        viewHolder.coverImg.setImageBitmap();
        Log.i(TAG, "setImageData image = " + image);
    }

    private class ArticleViewHolder {
        private TextView articleTitle;
        private TextView articleAuthor;
        private ImageView articleCover;
        private TextView articleContent;

        ArticleViewHolder(View convertView) {
            articleTitle = (TextView) convertView.findViewById(R.id.tv_article_item_title);
            articleAuthor = (TextView) convertView.findViewById(R.id.tv_article_item_author);
            articleCover = (ImageView) convertView.findViewById(R.id.iv_article_item_cover);
            articleContent = (TextView) convertView.findViewById(R.id.tv_article_item_content);
        }
    }

    private class SentenceViewHolder {
        private TextView sentenceContent;

        SentenceViewHolder(View convertView) {
            sentenceContent = (TextView) convertView.findViewById(R.id.vtv_sentence_item_content);
        }
    }

    private class MusicViewHolder {
        private ImageView musicCover;
        private TextView musicTitle;
        private TextView musicAuthor;

        MusicViewHolder(View convertView) {
            musicCover = (ImageView) convertView.findViewById(R.id.iv_music_item_cover);
            musicTitle = (TextView) convertView.findViewById(R.id.tv_music_item_title);
            musicAuthor = (TextView) convertView.findViewById(R.id.tv_music_item_author);
        }
    }

    private class ImageViewHolder {
        private ImageView coverImg;

        ImageViewHolder(View convertView) {
            coverImg = (ImageView) convertView.findViewById(R.id.iv_image_item_cover);
        }
    }
}
